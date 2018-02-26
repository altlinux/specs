Name:           suspend-utils
Version:        0.8
Release:        alt1
Summary:        A Set Of Tools To Support Sleep Modes
License:        GPLv2+
Url:            http://sourceforge.net/projects/suspend
#git		git://git.kernel.org/pub/scm/linux/kernel/git/rafael/suspend-utils.git
Group:          System/Base
Source:         %name-%version.tar
ExclusiveArch:  %ix86 x86_64

# Automatically added by buildreq on Thu Sep 09 2010
BuildRequires: libpci-devel libx86-devel perl-Switch

%description
A set of tools to support suspending notebooks, working around the
specific problems each machine has.

%prep
%setup -q

%build
autoreconf -fisv
%configure
%make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
/usr/sbin/s2ram

%changelog
* Thu Sep 09 2010 Anton Farygin <rider@altlinux.ru> 0.8-alt1
- first build for Sisyphus
