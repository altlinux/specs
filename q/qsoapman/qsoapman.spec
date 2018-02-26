Name: qsoapman
Version: 0.4
Release: alt1

Summary: Qt SOAP Manager
License: GPL
Group: Communications
Url: http://qsoapman.sf.net/

Source: %name-%version.tar.gz

BuildPreReq: gcc-c++ libqt3-devel

%description
Qt SOAP Manager is a GUI tool for sending SOAP messages. It can be used
for the development, debugging or exploration of Web Services. It is
written in C++ and should run on every platform supported by Qt.

%prep
%setup -q
%__rm -f src/Makefile

%build
export PATH=$PATH:/usr/lib/qt3/bin
qmake
%make_build

%install
%__mkdir_p %buildroot%_bindir/
%__install -p bin/%name %buildroot%_bindir/

%files
%_bindir/*
%doc AUTHORS ChangeLog INSTALL README TODO *.xml

%changelog
* Sun Aug 28 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.4-alt1
- initial build
