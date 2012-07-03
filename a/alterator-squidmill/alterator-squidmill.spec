%define _altdata_dir %_datadir/alterator

Name: alterator-squidmill
Version: 2.0
Release: alt5

Packager: Paul Wolneykien <manowar@altlinux.ru>

BuildArch: noarch

Source:%name-%version.tar.gz

Summary: Alterator module for browsing the Squid proxy server statistics
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.8-alt1
Requires: alterator-fbi >= 5.11-alt2
Requires: squidmill >= 2.0-alt3
Requires: alterator-service-functions >= 1.0
Conflicts: alterator >= 5.0
Conflicts: alterator-fbi >= 6.0
Conflicts: squidmill >= 3.0
Conflicts: alterator-service-functions >= 2.0

# Automatically added by buildreq on Wed Apr 08 2009
BuildRequires: alterator rpm-macros-fillup

%description
Alterator module for browsing the Squid proxy server statistics

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/squidmill
%_alterator_backend3dir/squidmill

%changelog
* Thu Mar 22 2012 Paul Wolneykien <manowar@altlinux.ru> 2.0-alt5
- Fix error reporting.

* Fri Mar 16 2012 Paul Wolneykien <manowar@altlinux.ru> 2.0-alt4
- Report squidmill errors.

* Tue Oct 20 2009 Paul Wolneykien <manowar@altlinux.ru> 2.0-alt3
- Remove metalterator dependence.

* Thu Oct 08 2009 Paul Wolneykien <manowar@altlinux.ru> 2.0-alt2
- Fix empty date parameter passing.

* Wed Oct 07 2009 Paul Wolneykien <manowar@altlinux.ru> 2.0-alt1
- Squidmill 2.0 based release.

* Mon Apr 27 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Missing Guile-lib-os requirement fixed.

* Wed Apr 22 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial release.
