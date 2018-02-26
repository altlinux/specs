Name: srpmcmp
Version: 0.3
Release: alt1

Summary: Compare source RPM packages
License: GPL or Artistic
Group: Development/Other
Url: http://altlinux.org
BuildArch: noarch

Source: %name

Requires: bzip2 cpio diffutils gzip rpm tar xz
BuildRequires: perl-Pod-Parser

%description
This perl script compares the contents of two source rpm packages
and outputs the difference in unified diff format.

%prep
%setup -cT
cp -avL %SOURCE0 %name

%build
pod2man %name > %name.1

%install
install -pD -m755 %name %buildroot%_bindir/%name
install -pD -m644 %name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/%name.*

%changelog
* Sun Nov 14 2010 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Updated build requirements.
- Fixed File::Temp use.
- Added xz(1) supprt.

* Wed Sep 29 2004 Alexey Tourbin <at@altlinux.ru> 0.2-alt3
- cleanups

* Sun Sep 26 2004 Alexey Tourbin <at@altlinux.ru> 0.2-alt2
- unpack also *.tgz
- enhanced autocrap detection

* Thu Sep 16 2004 Alexey Tourbin <at@altlinux.ru> 0.2-alt1
- added error handling
- added --verbose option
- enhanced autocrap detection
- optimized for speed

* Wed Dec 10 2003 Alexey Tourbin <at@altlinux.ru> 0.1-alt2
- trap signals
- RCS keyword unexpansion introduced

* Sun Nov 30 2003 Alexey Tourbin <at@altlinux.ru> 0.1-alt1
- initial revision
