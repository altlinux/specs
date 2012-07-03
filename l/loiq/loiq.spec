Name: loiq
Version: 0.2.3
Release: alt1

Summary: Low Orbit Ion Cannon ported to C++/Qt4
License: GPLv3
Group: Security/Networking

Url: http://sourceforge.net/projects/loiq/

Source: %name-%version.tar

BuildRequires: gcc-c++ libqt4-devel

%description
LOIQ stands for Low Orbit Ion Cannon in Qt. It is an attempt to port the famous
public-domain server stress-testing tool from C#/.Net to C++/Qt4, thus making it
available for the vast community of GNU/Linux users, as well as for the rest of
us *NIXoids.
LOIQ is a software that can create a large number of inbound requests to test
the ability of a server to withstand high load levels. Its primary use is
checking the webserver's fitness for serving a huge number of clients, although
other uses are feasible, wherever tolerance to high load is to be achieved.
Currently, it looks like all the features of the original software have been
implemented, although there are sound reasons to believe that the implementation
is way far from the optimal or even correct one. It also should be noted that
the project was undertaken mostly as an interesting case for practical learning
of Qt4 framework and C++ programming, therefore errors and failures are likely
to occur.

%prep
%setup

%build
%make_build

%install
install -pDm0755 %name %buildroot%_bindir/%name

%files
%_bindir/*
%doc README

%changelog
* Thu Dec 09 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus.

