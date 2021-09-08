%def_without check

%define oname constantly
Name: python3-module-%oname
Version: 15.1.0
Release: alt6

Summary: Symbolic constants in Python

Url: http://github.com/twisted/constantly
License: X11
Group: Development/Python3
BuildArch: noarch

# https://github.com/twisted/constantly.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(json)

%description
A library that provides symbolic constant support.
It includes collections and constants with text, numeric, and bit flag values.
Originally ``twisted.python.constants`` from the `Twisted <https://twistedmatrix.com/>`_ project.

%prep
%setup

# fix version info
sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: %version\)\"/" \
	%oname/_version.py

%build
%python3_build

%install
%python3_install

%check
py.test3

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Wed Sep 08 2021 Grigory Ustinov <grenka@altlinux.org> 15.1.0-alt6
- Build without python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 15.1.0-alt5.qa1
- NMU: applied repocop patch

* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 15.1.0-alt5
- Updated build dependencies.

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 15.1.0-alt4
- Fixed egg-info version.
- Explicitely stated egg-info including valid version.

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 15.1.0-alt3
- Fixed egg-info version.

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 15.1.0-alt2
- Enabled build for python-3.

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 15.1.0-alt1
- initial build for ALT Sisyphus

