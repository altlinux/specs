BuildArch: noarch
Name: ec2-ami-tools
Version: 1.4.0.7
Release: alt1
License: Amazon Software License
Group: Networking/Other
Summary: Tools for creating, bundling and uploading AMIs

Source: %name-%version.tar

Requires: rsync
Requires: ruby

%description
Tools for creating, bundling and uploading AMIs.
%prep
%setup
%build
./fix-bin
%install
mkdir -p %buildroot/usr/share/ruby/1.9
cp -a lib/ec2 %buildroot/usr/share/ruby/1.9/ec2
cp -a bin %buildroot/usr/bin
cp -a etc %buildroot/etc
%files
%dir %_sysconfdir/ec2
%dir %_sysconfdir/ec2/amitools
%config  %_sysconfdir/ec2/amitools/cert-ec2-gov.pem
%config  %_sysconfdir/ec2/amitools/cert-ec2.pem
%config  %_sysconfdir/ec2/amitools/mappings.csv
/usr/share/ruby/1.9/ec2
%_bindir/ec2-ami-tools-version
%_bindir/ec2-bundle-image
%_bindir/ec2-bundle-vol
%_bindir/ec2-delete-bundle
%_bindir/ec2-download-bundle
%_bindir/ec2-migrate-bundle
%_bindir/ec2-migrate-manifest
%_bindir/ec2-unbundle
%_bindir/ec2-upload-bundle
%doc license.txt notice.txt

%changelog
* Fri Apr 06 2012 Denis Smirnov <mithraen@altlinux.ru> 1.4.0.7-alt1
- 1.4.0.7
