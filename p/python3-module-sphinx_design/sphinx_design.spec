%define oname sphinx_design
Name: python3-module-%oname
Version: 0.2.0
Release: alt1
Summary: A sphinx extension for designing beautiful, view size responsive web components
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/sphinx_design
Source0: %oname-%version.tar.gz
BuildArch: noarch

# Automatically added by buildreq on Wed Jun 15 2022
# optimized out: libgpg-error python3 python3-base python3-dev python3-module-packaging python3-module-pep517 python3-module-pyparsing python3-module-tomli sh4
BuildRequires: python3-module-build python3-module-flit python3-module-setuptools

%description
%summary

%prep
%setup -n %oname-%version

%build
python3 -m build -w -n

%install
pip3 install --no-deps --root=%buildroot -I dist/*.whl

%files
%doc *.md
%python3_sitelibdir/%{oname}*

%changelog
* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 0.2.0-alt1
- Autobuild version bump to 0.2.0

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 0.0.1-alt1
- Initial version for ALT
