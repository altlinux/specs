Name: python3-module-linkheader
Version: 0.4.3
Release: alt1

Summary: Parse and format link headers according to RFC 5988
License: BSD
Group: Development/Python
Url: https://pypi.org/project/LinkHeader/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/link_header.py
%python3_sitelibdir/*/link_header.*
%python3_sitelibdir/LinkHeader-%version.dist-info

%changelog
* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.3-alt1
- 0.4.3 released

