%define module RPM-Source-Editor
%def_without hashertarbuild

Name: perl-%module
Version: 0.9204
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Perl library for src.rpm and spec file editing
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
#Url: http://search.cpan.org/dist/%module
Url: http://git.altlinux.org/people/viy/packages/RPM-Source-Editor.git

# due to rpmbuild -bE
# Recommends: rpm-build

# Automatically added by buildreq on Wed Nov 06 2010
BuildRequires: perl-devel /usr/bin/pod2man perl-podlators perl(RPM/Vercmp.pm) perl(RPM/Header.pm) perl(Clone.pm) perl(Tie/Hash.pm)
# for RPM::Source::Tools
BuildRequires: perl(RPM/uscan.pm) perl(Pod/Strip.pm) perl-Source-Shared-Resource
# for srpm-spec-inject-patches
BuildRequires: perl(Gear/Rules.pm)

Obsoletes: hashertarbuild < 0.73
Conflicts: hashertarbuild < 0.73

# recommends, in fact
Requires: pax

%description
Perl extension for editing src.RPMs and spec files

%if_with hashertarbuild
%package -n hashertarbuild
Group: Development/Other
Summary: a tool to create source tarballs for hasher
Requires: %name = %version-%release

%description -n hashertarbuild
A tool to create rpm-based source tarballs for hasher.
Sometimes rpmbuild -bs --nodeps does not work due to macros abcent. 
Use hashertarbuild <spec> to create source tarball ready for hasher.
%endif

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build 
#INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

install -m755 -D hashertarbuild %buildroot%_bindir/hashertarbuild
for i in hashertarbuild; do
    pod2man  --name $i --center 'hashertarbuild' --section 1 --release %version $i > $i.1
done

mkdir -p %buildroot%_man1dir
install -m 644 *.1 %buildroot%_man1dir/

mkdir -p %buildroot%_datadir/srpmtools/hooks

%files
%doc Changes
#doc README
%_bindir/srpm*
%perl_vendor_privlib/RPM*
#perl_vendor_man3dir/*
%dir %_datadir/srpmtools
%dir %_datadir/srpmtools/hooks
%_man1dir/srpm-spec-inject-patches*

#files -n hashertarbuild
%_bindir/hashertarbuild
%_man1dir/hashertarbuild*

%changelog
* Thu Jan 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.9204-alt1
- new version

* Tue Jan 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.9203-alt1
- new version

* Thu Dec 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.9202-alt1
- new version

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.9201-alt1
- new version

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.9200-alt1
- bugfix release

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.919-alt1
- development release

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.918-alt1
- bugfix release (closes: #30997)

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.917-alt1
- bugfix release

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.916-alt1
- development release

* Tue Oct 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.915-alt1
- bugfix release

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.914-alt1
- bugfix release

* Thu May 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.913-alt1
- %%ubt changelog bugfixes (closes: #33442)

* Sat May 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.912-alt1
- proper %%ubt support in changelog (closes: #33442)

* Sat May 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.911-alt1
- development release

* Sun Apr 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.910-alt1
- bugfix release

* Mon Feb 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.909-alt1
- development release

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.908-alt1
- added srpm-spec-inject-patches

* Mon Feb 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.907-alt1
- development release

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.906-alt1
- development release

* Thu Feb 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.905-alt1
- development release

* Wed Feb 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.904-alt1
- stable release

* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.903-alt1
- development release

* Mon Jan 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.902-alt1
- development release

* Fri Jan 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.901-alt1
- development release

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.900-alt1
- development release

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.899-alt1
- stable release

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.898-alt1
- development release

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.897-alt1
- development release

* Mon Jan 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.896-alt1
- development release

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.895-alt1
- development release

* Thu Jan 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.894-alt1
- development release

* Wed Jan 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.893-alt1
- development release

* Sun Jan 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.892-alt1
- development release

* Wed Dec 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.891-alt1
- development release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.890-alt1
- development release

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.889-alt1
- stable release

* Tue Nov 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.888-alt1
- more command line transformation options

* Wed Nov 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.887-alt1
- development release

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.886-alt1
- development release

* Mon Oct 31 2016 Igor Vlasenko <viy@altlinux.ru> 0.885-alt1
- development release; add_patch DISABLE

* Mon Oct 31 2016 Igor Vlasenko <viy@altlinux.ru> 0.884-alt1
- development release; added COMMENTED to add_patch

* Sun Oct 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.883-alt1
- development release; changed rename_package behaviour

* Mon Oct 24 2016 Igor Vlasenko <viy@altlinux.ru> 0.882-alt1
- bugfix release

* Thu Oct 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.881-alt1
- development release

* Tue Oct 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.880-alt1
- bugfix release

* Tue Oct 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.879-alt1
- development release

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.878-alt3
- use no RPM::Database

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.878-alt2
- use RPM::Header

* Mon Oct 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.878-alt1
- use RPM::Vercmp

* Thu Sep 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.877-alt1
- support for plain SourceXX: watch (closes: #32521)

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.876-alt1
- development release

* Wed Jul 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.875-alt1
- development release

* Mon Jul 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.874-alt1
- stable release

* Mon Jun 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.873-alt1
- bugfix release

* Fri May 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.872-alt1
- stable release

* Thu Apr 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.871-alt1
- development release

* Sat Apr 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.870-alt1
- stable release

* Fri Apr 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.869-alt1
- development release

* Tue Apr 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.868-alt1
- bugfix release

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.867-alt1
- development release

* Tue Apr 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.866-alt1
- development release

* Sun Mar 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.865-alt1
- development release

* Tue Mar 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.864-alt1
- development release

* Tue Mar 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.863-alt1
- development release

* Sun Mar 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.862-alt1
- development release

* Sun Mar 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.861-alt1
- stable release

* Tue Mar 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.860-alt1
- development release

* Sun Feb 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.859-alt1
- stable release

* Sat Feb 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.858-alt1
- stable release

* Mon Feb 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.857-alt1
- bugfix release

* Sat Feb 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.856-alt1
- development release

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.855-alt1
- development release

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.854-alt1
- development release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.853-alt1
- rpm 4.13 support

* Sat Jan 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.852-alt1
- development release

* Sat Jan 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.851-alt1
- development release

* Sat Dec 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.850-alt1
- bugfix release

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 0.849-alt1
- development release

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.848-alt1
- bugfix release

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 0.847-alt1
- bugfix release

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.846-alt1
- development release

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.845-alt1
- bugfix release

* Sun Aug 23 2015 Igor Vlasenko <viy@altlinux.ru> 0.844-alt1
- added before_process_options

* Thu Dec 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.843-alt1
- development release

* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.842-alt1
- development release

* Sun Jun 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.841-alt1
- development release

* Mon Jun 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.840-alt1
- development release

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.839-alt1
- development release

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.838-alt1
- development release

* Thu May 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.837-alt1
- development release

* Wed May 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.836-alt1
- development release

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.835-alt1
- bugfix release

* Thu May 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.834-alt1
- bugfix release

* Wed Apr 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.833-alt1
- development release

* Wed Apr 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.832-alt1
- development release

* Fri Apr 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.831-alt1
- development release

* Mon Apr 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.830-alt1
- development release

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.826-alt1
- bugfix release

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.825-alt1
- bugfix release

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.824-alt1
- development release

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.823-alt1
- bugfix release

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.822-alt1
- bugfix release

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.821-alt1
- bugfix release

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.820-alt1
- bugfix release

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.819-alt1
- bugfix release

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.818-alt1
- development release

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.817-alt1
- bugfix release

* Thu Sep 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.816-alt1
- bugfix release

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.815-alt1
- development release

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.814-alt1
- development release

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.813-alt1
- development release

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.812-alt1
- development release

* Wed Aug 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.811-alt1
- development release; new API

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.810-alt1
- bugfix release

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.809-alt1
- development release

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.808-alt1
- bugfix release

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.807-alt1
- bugfix release

* Tue Apr 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.806-alt1
- bugfix release

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.805-alt1
- development release

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.804-alt1
- bugfix release

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.803-alt1
- bugfix release

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.802-alt1
- development release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.801-alt1
- added DependencyFilterFactory

* Sun Feb 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.800-alt1
- development release
