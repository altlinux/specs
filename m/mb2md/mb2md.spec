# -*- coding: latin-1; mode: rpm-spec -*-

Name: mb2md
Version: 3.20
Release: alt1

Summary: Converting Mbox mailboxes to Maildir format
License: Public domain
Group: File tools
Url: http://batleth.sapienti-sat.org/projects/mb2md/
Source: %name-%version.pl.gz
BuildArch: noarch

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildRequires: perl-TimeDate

%description
Converting Mbox mailboxes to Maildir format

%prep
%setup -cT
cp -av %SOURCE0 %name.gz
gzip -d %name.gz

%build
%install
install -m 755 -D %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Sat Apr 10 2010 Terechkov Evgenii <evg@altlinux.ru> 3.20-alt1
- Initial build for ALT Linux Sisyphus
