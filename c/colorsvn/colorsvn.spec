# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl perl(IPC/Open3.pm) perl(Term/ANSIColor.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           colorsvn
Version:        0.3.3
Release:        alt1_2
Epoch:          0
Summary:        Colorizer for subversion, based on colorgcc and colorcvs
Group:          Development/Other
License:        GPL
URL:            http://colorsvn.tigris.org/
Source0:        http://colorsvn.tigris.org/files/documents/4414/49311/colorsvn-%{version}.tar.gz
Requires:       subversion
BuildRequires:  subversion
BuildArch:      noarch
Source44: import.info

%description
Subversion output colorizer.

%prep
%setup -q

%build
%configure

%install
%{makeinstall_std}
/usr/bin/perl -p -e 's|/bin/sh|/bin/csh|;' \
             -e 's|=| |g;' \
  %{buildroot}%{_sysconfdir}/profile.d/colorsvn-env.sh \
  > %{buildroot}%{_sysconfdir}/profile.d/colorsvn-env.csh

%files
%doc ChangeLog COPYING CREDITS INSTALL
%attr(0755,root,root) %{_bindir}/colorsvn
%{_mandir}/man1/colorsvn.1*
%config(noreplace) %{_sysconfdir}/colorsvnrc
%attr(0755,root,root) %{_sysconfdir}/profile.d/colorsvn-env.sh
%attr(0755,root,root) %{_sysconfdir}/profile.d/colorsvn-env.csh






%changelog
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 0:0.3.3-alt1_2
- new version

