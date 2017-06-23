%define sendmail %_sbindir/sendmail

Name: msmtp
Version: 1.6.6
Release: alt1
Summary: Minimal SMTP client
License: GPL3+
Group: Networking/Mail
URL: http://msmtp.sf.net
Source0: %{name}-%{version}.tar.xz
BuildRequires: openssl-devel
BuildRequires: makeinfo

# Most build environments safely override this
#BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
The msmtp transmits a mail to a smarthost (an SMTP server
which takes care of further delivery) - just tell your MUA
to run msmtp instead of %sendmail


%package sendmail
Summary: %sendmail symlink for %name
Group: Networking/Mail
Requires: %{name} = %{version}
Provides: %sendmail
Provides: MTA
Conflicts: sendmail, sendmail-submit
Conflicts: ssmtp, ssmtp-ssl
Conflicts: postfix-sendmail, exim-sendmail
BuildArch: noarch

%description sendmail
This package provides %summary


%package info
Summary: .info files for %name
Group: Networking/Mail
BuildArch: noarch

%description info
This package provides %summary


%prep
%setup


%build
%configure \
  --disable-rpath \
  --with-ssl=openssl \
  --without-libgsasl \
  --without-libidn
%make_build


%install
%makeinstall
mkdir -m 700 -p %{buildroot}%{_sysconfdir}/skel
rm -rf %{buildroot}%{_datadir}/locale
install -m 600 %{name}rc.skel \
  %{buildroot}%{_sysconfdir}/skel/.%{name}rc
mkdir -pm755 %{buildroot}%{_sbindir}
ln -s ../bin/%{name} %{buildroot}%{sendmail}


%files
%{_bindir}/*
%{_man1dir}/*
%config(noreplace) %{_sysconfdir}/skel/.%{name}rc

%files sendmail
%{sendmail}

%files info
%{_infodir}/*

%changelog
* Fri Jun 23 2017  Alexey V. Vissarionov <gremlin@altlinux.org> 1.6.6-alt1
- Updated to 1.6.6
- Fixed RFC-821 violation by empty domain name
- Rewrote the .spec from a scratch

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.4.27-alt1.1
- NMU: added BR: texinfo

