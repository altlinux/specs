# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl
# END SourceDeps(oneline)
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name ddccontrol-db
%define version 20061014
%global git_commit e8cc385a6321e7c99783150001193ec6e9e0c436
%global git_date 20120904

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

# git clone git://ddccontrol.git.sourceforge.net/gitroot/ddccontrol/ddccontrol-db
# cd ddccontrol-db
# git archive --format=tar --prefix=%%{name}-%%{version}/ %%{git_commit} | \
# bzip2 > ../%%{name}-%%{version}-%%{git_suffix}.tar.bz2

Name:             ddccontrol-db
URL:              http://ddccontrol.sourceforge.net/
Version:          20061014
Release:          alt1_8.%{git_suffix}
# Agreed by usptream to be GPLv2+
# http://sourceforge.net/mailarchive/message.php?msg_id=29762202
License:          GPLv2+
Group:            File tools
Summary:          DDC/CI control database for ddccontrol
#Source0:          http://downloads.sourceforge.net/ddccontrol/%{name}-%{version}.tar.bz2
Source0:          %{name}-%{version}-%{git_suffix}.tar.bz2
# use autopoint instead of gettextize that is interactive tool
Patch0:           %{name}-autopoint.patch
BuildRequires: gettext gettext-tools gettext-tools-python gettext-tools libasprintf-devel, libtool-common, perl(XML/Parser.pm)
BuildArch:        noarch
Source44: import.info
Patch33: ddccontrol-db-0.4.2-russian.patch
Conflicts: ddccontrol < 0.4.2-alt15

%description
DDC/CU control database for DDCcontrol.

%prep
%setup -q
%patch0 -p1 -b .autopoint

./autogen.sh
%patch33 -p2

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_datadir}/%{name}

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_8.20120904gite8cc385a
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_7.20120904gite8cc385a
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_6.20120904gite8cc385a
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_5.20120904gite8cc385a
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_4.20120904git%(echo e8cc385a6321e7c99783150001193ec6e9e0c436 | cut -c -8)
- update to new release by fcimport

* Wed Dec 19 2012 Igor Vlasenko <viy@altlinux.ru> 20061014-alt1_3.20120904gite8cc385a
- fc import for more frequent updates

