Group: Office
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/desktop-file-validate gcc-c++ perl(DBD/Pg.pm) perl(Encode.pm) perl(Pod/Usage.pm) perl(Term/Cap.pm) perl(Term/ReadKey.pm) perl(Wx.pm) perl(Wx/App.pm) perl(Wx/Event.pm) perl(Wx/FS.pm) perl(Wx/Help.pm) perl(Wx/Html.pm) perl(Wx/Locale.pm) perl(YAML.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# -*- rpm-spec -*-

################ Build Options ###################
%define dbtests 1
%{?_with_dbtests:    %{expand: %%global dbtests 1}}
%{?_without_dbtests: %{expand: %%global dbtests 0}}
%define debug_package %{nil}
################ End Build Options ################

Name: EekBoek
Summary: Bookkeeping software for small and medium-size businesses
License: GPL+ or Artistic
Version: 2.051
Release: alt2
Source: https://www.eekboek.nl/dl/%{name}-%{version}.tar.gz
URL: https://www.eekboek.nl
Packager: Ilya Mashkin <oddity@altlinux.ru>
# The package name is CamelCased. However, for convenience some
# of its data is located in files and directories that are all
# lowercase. See the %%install section.
%global lcname eekboek

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

# This package would provide many (perl) modules, but these are
# note intended for general use.
AutoReqProv: 0

Requires: rpm-build-perl
Requires: perl
Requires: perl(Archive/Zip.pm)
Requires: perl(HTML/Parser.pm)
Requires: perl(Term/ReadLine.pm)
Requires: perl(Term/ReadLine/Gnu.pm)
Requires: perl(DBI.pm) >= 1.400
Requires: perl(DBD/SQLite.pm) >= 1.120
Requires: perl(App/Packager.pm) >= 1.430

BuildRequires: perl-devel
BuildRequires: rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(IPC/Run3.pm)
BuildRequires: perl(Archive/Zip.pm)
BuildRequires: perl(HTML/Parser.pm)
BuildRequires: perl(Term/ReadLine.pm)
BuildRequires: perl(Term/ReadLine/Gnu.pm)
BuildRequires: perl(DBI.pm)
BuildRequires: perl(DBD/SQLite.pm)
BuildRequires: perl(App/Packager.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: desktop-file-utils
BuildRequires: zip

Obsoletes: %{name}-core < 2.00.01
Obsoletes: %{name}-contrib < 2.00.01
Conflicts: %{name}-core < 2.00.01

# For symmetry.
%global __zip   /usr/bin/zip
%global __rmdir /bin/rmdir
%global __find  /usr/bin/find
Source44: import.info

%description
EekBoek is a bookkeeping package for small and medium-size businesses.
Unlike other accounting software, EekBoek has both a command-line
interface (CLI) and a graphical user-interface (GUI, currently under
development and not included in this package). Furthermore, it has a
complete Perl API to create your own custom applications. EekBoek is
designed for the Dutch/European market and currently available in
Dutch only. An English translation is in the works (help appreciated).

EekBoek can make use of several database systems for its storage.
Support for the SQLite database is included.

For GUI support, install %{name}-gui.

For production use, you are invited to install the %{name}-db-postgresql
database package.

%package gui
Group: Other

Summary: %{name} graphical user interface
AutoReqProv: 0

Requires: %{name} = %{version}-%{release}
Requires: perl(Wx.pm) >= 0.990

%description gui
This package contains the wxWidgets (GUI) extension for %{name}.

%package db-postgresql
Group: Other

# This package only contains the necessary module(s) for EekBoek
# to use the PostgreSQL database.
# Installing this package will pull in the main package and
# the Perl PostgreSQL modules, if necessary.
# No %%doc required.

Summary: PostgreSQL database driver for %{name}
AutoReqProv: 0
Requires: %{name} = %{version}-%{release}
Requires: perl(DBD/Pg.pm) >= 1.410

%description db-postgresql
EekBoek can make use of several database systems for its storage.
This package contains the PostgreSQL database driver for %{name}.

%prep
%setup -q

chmod 0664 MANIFEST

%build
/usr/bin/perl Makefile.PL
make

# Move some files into better places.
mkdir examples
mv emacs/eekboek-mode.el examples

%install

# Short names for our libraries.
%global ebconf  %{_sysconfdir}/%{lcname}
%global ebshare %{_datadir}/%{name}-%{version}

mkdir -p %{buildroot}%{ebconf}
mkdir -p %{buildroot}%{ebshare}/lib
mkdir -p %{buildroot}%{_bindir}

# Install the default, system-wide config file.
install -p -m 0644 blib/lib/EB/examples/%{lcname}.conf %{buildroot}%{ebconf}/%{lcname}.conf

# Create lib dirs and copy files.
%{__find} blib/lib -type f -name .exists -delete
%{__find} blib/lib -depth -type d -name auto -exec rm -fr {} \;
%{__find} blib/lib -type d -printf "mkdir %{buildroot}%{ebshare}/lib/%%P\n" | sh -x
%{__find} blib/lib ! -type d -printf "install -p -m 0644 %p %{buildroot}%{ebshare}/lib/%%P\n" | sh -x

for script in ebshell ebwxshell
do

  # Create the main scripts.
  echo "#!%{__perl}" > %{buildroot}%{_bindir}/${script}
  sed -s "s;# use lib qw(EekBoekLibrary;use lib qw(%{ebshare}/lib;" \
    < script/${script} >> %{buildroot}%{_bindir}/${script}
  chmod 0755 %{buildroot}%{_bindir}/${script}

  # And its manual page.
  mkdir -p %{buildroot}%{_mandir}/man1
  pod2man blib/script/${script} > %{buildroot}%{_mandir}/man1/${script}.1

done

# Desktop file, icons, ...
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 0664 lib/EB/res/Wx/icons/ebicon.png %{buildroot}%{_datadir}/pixmaps/
for script in ebwxshell
do
  desktop-file-install --delete-original \
    --dir=%{buildroot}%{_datadir}/applications ${script}.desktop
  desktop-file-validate %{buildroot}/%{_datadir}/applications/${script}.desktop
done

# End of install section.

%check
%if %{dbtests}
make test
%else
env EB_SKIPDBTESTS=1 make test
%endif

%files
%doc CHANGES README examples/
%dir %{_sysconfdir}/%{lcname}
%config(noreplace) %{_sysconfdir}/%{lcname}/%{lcname}.conf
%{ebshare}/
%exclude %{ebshare}/lib/EB/DB/Postgres.pm
%exclude %{ebshare}/lib/EB/Wx
%{_bindir}/ebshell
%{_mandir}/man1/ebshell*

%files gui
%doc README.gui
%{ebshare}/lib/EB/Wx
%{_bindir}/ebwxshell
%{_mandir}/man1/ebwxshell*
%{_datadir}/applications/ebwxshell.desktop
%{_datadir}/pixmaps/ebicon.png

%files db-postgresql
%doc README.postgres
%{ebshare}/lib/EB/DB/Postgres.pm

%changelog
* Sat Dec 24 2022 Ilya Mashkin <oddity@altlinux.ru> 2.051-alt2
- Build for Sisyphus
- Change Group to Office

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 2.051-alt1_4
- update to new release by fcimport

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 2.051-alt1_3
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 2.051-alt1_2
- update to new release by fcimport

* Mon Sep 20 2021 Igor Vlasenko <viy@altlinux.org> 2.051-alt1_1
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 2.04-alt1_3
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 2.04-alt1_2
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 2.03-alt2_13
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1_13
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1_12
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1_11
- update to new release by fcimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1_10
- new version

