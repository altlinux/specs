
%define base_name omemo-dr
%define base_name2 omemo_dr
Name: python3-module-%base_name
Version: 1.0.0
Release: alt1
Summary: OMEMO Double Ratchet
License: GPLv3
Group: Development/Python3
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: https://dev.gajim.org/gajim/omemo-dr
Source: %base_name-%version.tar.gz
BuildRequires: python3-module-pip python3-module-setuptools_scm
BuildRequires: rpm-build-python3 python3-module-setuptools rpm-macros-python3 pyproject-build  python3-module-build
#BuildArch: noarch

%description
OMEMO Double Ratchet. Initial codebase was forked from python-axolotl but has since been heavily rewritten.
This library handles only the crypto part of OMEMO, not the XMPP protocol part.

%prep
%setup -n %base_name-%version

%build
%python3_build

%install
%python3_install


%files
%python3_sitelibdir/%base_name2
%python3_sitelibdir/%base_name2-%version-py?.??.egg-info
#_bindir/python3-%base_name2


%changelog
* Sun May 28 2023 Ilya Mashkin <oddity@altlinux.ru> 1.0.0-alt1
- Initial build for Sisyphus

