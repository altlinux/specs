Name: gnu-config
Version: 1.0.603.062587e
Release: alt1

Summary: GNU config.guess and config.sub files
License: GPLv2+
Group: Development/Other
Url: http://git.savannah.gnu.org/gitweb/?p=config.git
BuildArch: noarch

# git://git.altlinux.org/gears/g/gnu-config.git
Source: %name-%version-%release.tar

%description
This packages contains a recent revision of GNU config.guess and
config.sub files.

%prep
%setup -n %name-%version-%release

%check
%make_build -k check

%install
mkdir -p %buildroot%_datadir/%name
install -pm755 config.guess config.sub %buildroot%_datadir/%name/
%add_findreq_skiplist %_datadir/%name/config.guess

%files
%_datadir/%name/

%changelog
* Mon Aug 20 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.603.062587e-alt1
- Updated to release-1-0-603-g062587e.

* Fri Aug 17 2012 Dmitry V. Levin <ldv@altlinux.org> 1.0.602.6f8e28f-alt1
- Built GNU config.git release-1-0-602-g6f8e28f for Sisyphus.
- config.sub: Added armh support as proposed by Sergey Bolshakov.
