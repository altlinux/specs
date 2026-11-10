%define pypi_name rank_bm25

Name: python3-module-rank-bm25
Version: 0.2.2
Release: alt1
Summary: BM25 algorithms for document ranking

License: Apache-2.0
Group: Development/Python3
URL: https://github.com/dorianbrown/rank_bm25
# Source-url: https://github.com/dorianbrown/rank_bm25/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Patch1: 0001-build-version.patch
BuildArch: noarch
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3 python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-numpy

%description
BM25 algorithms for document ranking.

%prep
%setup
%patch1 -p1

%build
export RANK_BM25_BUILD_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
python3 - <<'CHECK'
from rank_bm25 import BM25Okapi
corpus = ["chromium renders local pages", "python packages libraries", "redis stores data"]
ranker = BM25Okapi([text.split() for text in corpus])
assert ranker.get_top_n(["chromium"], corpus, n=1) == [corpus[0]]
CHECK

%files
%python3_sitelibdir/rank_bm25.py
%python3_sitelibdir/__pycache__/rank_bm25.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README.md LICENSE

%changelog
* Thu Nov 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1
- initial build for ALT Sisyphus

