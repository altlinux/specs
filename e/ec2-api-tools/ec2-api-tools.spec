BuildArch: noarch
Name: ec2-api-tools
Version: 1.5.6.0
Release: alt1
License: Amazon Software License
Group: Networking/Other
Summary: EC2 utilites

URL: http://aws.amazon.com/developertools/
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

%description
%summary

%prep
%setup
%build
./fix-bin
cp -f ec2-cmd bin/ec2-cmd
%install
mkdir -p %buildroot/usr/bin %buildroot%_datadir/%name
install -m 644 -D lib/*.jar %buildroot%_datadir/%name
install -m 755 -D bin/*  %buildroot/usr/bin

%files
%_bindir/*
%_datadir/ec2-api-tools/*
%doc license.txt notice.txt

%changelog
* Tue Jul 10 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.6.0-alt1
- 1.5.6.0

* Mon Jun 18 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.5.0-alt1
- 1.5.5.0

* Mon Apr 09 2012 Denis Smirnov <mithraen@altlinux.ru> 1.5.2.5-alt1
- initial build for ALT Linux Sisyphus

