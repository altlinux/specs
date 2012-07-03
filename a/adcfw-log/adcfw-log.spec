Summary: Tool for analyzing firewall logs
Name: adcfw-log
Version: 0.10.0
Release: alt1.qa1
License: GPL
Group: Monitoring
Url: http://adcfw-log.sourceforge.net/
Packager: Mikhail Pokidko <pma@altlinux.org>

Source: %name-%version.tar.gz

BuildRequires: perl >= 5.6.1
Requires: perl >= 5.6.1

%description
adcfw-log is a tool for analyzing firewall logs in order to extract
meaningful information. It is designed to be a standalone script
with very few requirements that can generate different kinds of
reports, such as fully formatted reports of what had been logged,
with summaries by source or destination host, the type of service,
or protocol. There are also options to filter the input data by date,
host, protocol, service, and so on.

Only netfilter log format (linux kernel 2.4.x) is supported at this time.

%prep
%setup

%build
%configure
make %{?_smp_mflags}

%install
%makeinstall

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %_mandir/man?/*
%_bindir/*

%changelog
* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.10.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for adcfw-log
  * postclean-05-filetriggers for spec file

* Wed Aug 15 2007 Pokidko Mikhail <pma@altlinux.org> 0.10.0-alt1
- initial ALT build

