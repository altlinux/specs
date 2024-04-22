%define  oname OSlash

%def_with check

Name:    python3-module-%oname
Version: 0.6.3
Release: alt4

Summary: Functors, Applicatives, And Monads in Python

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/OSlash
VCS:     https://github.com/dbrattli/OSlash

Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-typing_extensions
%endif

BuildArch: noarch

%description
OSlash is a library for playing with functional programming in Python 3.8+.
It's an attempt to re-implement some of the code from Learn You a Haskell
for Great Good! in Python 3.8. OSlash unifies functional and object oriented
paradigms by grouping related functions within classes. Objects are however
never used for storing values or mutable data, and data only lives within
function closures.

OSlash is intended to be a tutorial. For practical functional programming
in Python in production environments you should use FSlash instead.

%prep
%setup
sed -i 's|"version": "0+unknown"|"version": "%version"|' versioneer.py
# hotfix for python3.12
sed -i 's/SafeConfigParser/ConfigParser/' versioneer.py
sed -i 's/readfp/read_file/' versioneer.py

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE *.md
%python3_sitelibdir/oslash
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Apr 22 2024 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt4
- Very tiny spec refactoring.

* Thu Jan 25 2024 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt3
- Fixed FTBFS.

* Thu Oct 06 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt2
- Use modern macros.
- Build with check.

* Fri Apr 08 2022 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus.
