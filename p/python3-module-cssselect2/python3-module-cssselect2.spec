%define  modulename cssselect2

Name:    python3-module-%modulename
Version: 0.2.1
Release: alt1

Summary: cssselect2 is a straightforward implementation of CSS3 Selectors for markup documents
License: BSD
Group:   Development/Python3
URL:     https://pypi.org/project/cssselect2/

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Sat Jun 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.1-alt1
- Initial build for ALT
