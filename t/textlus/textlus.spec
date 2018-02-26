
Name: textlus
Version: 0.5.0
Release: alt1
Summary: The utility to read large text files with speech synthesizer
Group: Sound
License: %gpl3plus
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildRequires: emacs23 emacs-devel
BuildRequires: rpm-build-licenses
BuildRequires: gcc-c++
Requires: RHVoice aplay

Source: %name-%version.tar.gz
Source1: site-start.el
Source2: read-book

%package -n emacs-%name
Summary: The tool for emacs to keep list of books to read with %name
Group: Sound
License: %gpl3plus
BuildArch: noarch
Requires: emacs-base emacs-elib
Requires: %name = %version-%release aplay

%description 
The utility to read large text files with speech synthesizer

%description -n emacs-%name
The tool for emacs to keep list of books to read with %name

%prep
%setup -q
%build
%configure
%make_build
%byte_compile_file eemacs/textlus.el

%install
make DESTDIR=%buildroot install
%__rm -f %buildroot%_datadir/%name/replacements
%__install -pD -m 644 data/replacements.rus %buildroot%_datadir/%name/replacements

%__install -d %buildroot%_emacslispdir
%__install -pD -m644 emacs/textlus.* %buildroot%_emacslispdir
%__install -d %buildroot%_emacs_sitestart_dir
%__install -pD -m 644 %SOURCE1 %buildroot%_emacs_sitestart_dir/textlus.el

%__install -pD -m 755 %SOURCE2 %buildroot%_bindir/read-book

%files
%doc AUTHOR ChangeLog COPYING NEWS README
%_bindir/*
%_datadir/%name

%files -n emacs-%name
%_emacslispdir/*
%_emacs_sitestart_dir/*

%changelog
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

