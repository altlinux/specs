Name: python3-module-pathspec
Version: 0.5.9
Release: alt1
Summary: Utility library for gitignore style pattern matching of file paths
License: MPLv2.0
Group: Development/Python
Url: https://github.com/cpburnz/python-path-specification

BuildArch: noarch

Source: %name-%version.tar

#BuildPreReq: rpm-build-python3
#BuildPreReq: python3-module-distribute
#BuildPreReq: python-module-epydoc

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-module-PyStemmer python-module-Pygments python-module-cssselect python-module-docutils python-module-pytz python-module-setuptools python-module-snowballstemmer python-modules python-modules-compiler python-modules-email python-modules-encodings python3 python3-base
BuildRequires: rpm-build-python3 python3-module-setuptools python3-module-sphinx

%description
pathspec is a utility library for pattern matching of file paths. So
far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its
gitignore files.

%prep
%setup

%build
%python3_build
%make_build doc

%install
%python3_install

%files
%python3_sitelibdir/*
%doc *.rst

%changelog
* Wed Sep 25 2019 Terechkov Evgenii <evg@altlinux.org> 0.5.9-alt1
- Initial build for ALT Linux Sisyphus
