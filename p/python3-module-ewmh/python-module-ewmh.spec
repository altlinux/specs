%define modulename ewmh

%def_with test

Name: python3-module-%modulename
Version: 0.1.6
Release: alt3
Summary: An implementation of EWMH (Extended Window Manager Hints) for python, based on Xlib

License: GPLv3
Group: Development/Python3
Url: https://github.com/parkouss/pyewmh
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-xlib
%py3_provides %modulename


%description
An implementation of EWMH (Extended Window Manager Hints) for python, based on
Xlib. It allows EWMH-compliant window managers (most modern WMs) to be queried
and controlled.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export LC_ALL=en_US.UTF-8
%__python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/*


%changelog
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.6-alt3
- Build for python2 disabled.

* Mon Mar 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt2
- Updated build dependencies.

* Mon Jan 02 2017 Anton Midyukov <antohami@altlinux.org> 0.1.6-alt1
- Initial build for ALT Linux.
