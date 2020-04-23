#!/usr/bin/env bash
this_dir="$( cd "$( dirname "$0" )" && pwd )"
export voice2json_dir="$(realpath "${this_dir}")"

venv="${this_dir}/.venv"

if [[ -d "${venv}" ]]; then
    # Use virtual environment
    source "${venv}/bin/activate"

    if [[ -d "${venv}/tools" ]]; then
        export LD_LIBRARY_PATH="${venv}/tools:${venv}/tools/lib:${LD_LIBRARY_PATH}"
        export PATH="${venv}/tools:${venv}/tools/bin:${PATH}"

        KALDI_DIR="${venv}/tools/kaldi"
        if [[ -d "${KALDI_DIR}" ]]; then
            export KALDI_DIR
        fi

        if [[ -d "${venv}/tools/precise-engine" ]]; then
            export PATH="${venv}/tools/precise-engine:${PATH}"
        fi
    fi
fi

export PYTHONPATH="${this_dir}"
export PATH="${this_dir}/bin:${PATH}"

python3 -m voice2json "$@"
