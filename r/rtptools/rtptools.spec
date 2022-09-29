Name: rtptools
Version: 1.23
Release: alt1

Summary: RTP Tools
License: BSD-3-Clause
Group: Networking/Other
Url: https://github.com/irtlab/rtptools

Source0: %name-%version-%release.tar

%description
The rtptools distribution consists of a number of small applications that
can be used for processing RTP data.
See http://www.cs.columbia.edu/IRT/software/rtptools

%prep
%setup
echo -e 'CC=gcc\nCFLAGS="%optflags -fcommon"' > configure.local

%build
sh configure
make

%install
%make_install BINDIR=%buildroot%_bindir MANDIR=%buildroot%_mandir install

%files
%doc LICENSE README*
%_bindir/*
%_man1dir/*

%changelog
* Thu Sep 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.23-alt1
- initial
