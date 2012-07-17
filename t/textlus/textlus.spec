
Name: textlus
Version: 0.99
Release: alt1
Summary: The utility to read large text files with speech synthesizer
Group: Sound
License: %gpl3plus
URL: http://www.marigostra.ru/projects/textlus/
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildRequires: rpm-build-licenses gcc-c++ make

Source: %name-%version.tar.gz

%description 
The utility to read large text files with speech synthesizer.

%prep
%setup -q
%build
make

%install
%__install -pD -m755 textlus %buildroot%_bindir/textlus

%files
%doc AUTHOR COPYING
%_bindir/*

%changelog
* Thu Jun 28 2012 Michael Pozhidaev <msp@altlinux.ru> 0.99-alt1
- New version
- RHVoice related scripts removed (will be moved into separate package)
- No more emacs subpackage (emacs add-ons will be part of Homeros scripts)

* Fri Sep 30 2011 Michael Pozhidaev <msp@altlinux.ru> 0.5.0-alt1
- New version

* Wed Apr 20 2011 Michael Pozhidaev <msp@altlinux.ru> 0.4.0-alt1
- New version
- Added read-book script

* Mon Apr 11 2011 Michael Pozhidaev <msp@altlinux.ru> 0.3.0-alt3
- Improved emacs front-end

* Sat Apr 09 2011 Michael Pozhidaev <msp@altlinux.ru> 0.3.0-alt2
- Added forgotten dependency between textlus and emacs-textlus packages

* Thu Apr 07 2011 Michael Pozhidaev <msp@altlinux.ru> 0.3.0-alt1
- INitial package

