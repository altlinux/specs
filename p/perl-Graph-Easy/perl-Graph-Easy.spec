# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Devel/Size.pm) perl(File/Find/Object.pm) perl(HTML/TokeParser.pm) perl(IO/All.pm) perl(LWP.pm) perl(Pod/Usage.pm) perl(Test/Run/CmdLine/Iface.pm) perl-podlators
# END SourceDeps(oneline)
%filter_from_requires /^perl.Graph.Easy.As_svg/d
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
Name:           perl-Graph-Easy
Version:        0.76
Release:        alt1_1
Summary:        Convert or render graphs as ASCII, HTML, SVG or via Graphviz
License:        GPLv2+ and ASL 1.1
Group:          Development/Other
URL:            http://search.cpan.org/dist/Graph-Easy/
Source0:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/Graph-Easy-%{version}.tar.gz
Patch0:         graph-easy-undefined-lc.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  rpm-build-perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Pod/Coverage.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/Differences.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(utf8.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)
Requires:       perl(Carp.pm)
Requires:       perl(Data/Dumper.pm)

# avoid circular dependencies
%bcond_without bootstrap
%if %{without bootstrap}
BuildRequires:  perl(Graph/Easy/As_svg.pm)
Requires:       perl(Graph/Easy/As_svg.pm) >= 0.23
%endif

# filter unversioned provides


Source44: import.info
%filter_from_provides /perl\\(Graph.Easy.pm\\)$/d
%filter_from_provides /perl\\(Graph.Easy.(Edge|Edge.Cell|Group|Node).pm\\)$/d

%description
Graph::Easy lets you generate graphs consisting of various shaped nodes
connected by edges (with optional labels). It can read and write graphs in a
variety of formats, as well as render them via its own grid-based layouter.
Since the layouter works on a grid (manhattan layout), the output is most
useful for flow charts, network diagrams, or hierarchy trees.

%prep
%setup -q -n Graph-Easy-%{version}
%patch0 -p 1

chmod 0644 examples/*

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES LICENSE README TODO examples
%{_bindir}/*
%{_mandir}/man1/*
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.76-alt1_1
- update to new release by fcimport

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.76-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.75-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.75-alt1_3
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.75-alt1_1
- update to new release by fcimport

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.75-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.73-alt2_3
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_2
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_1
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1_2
- update to new release by fcimport

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1_3
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1_1
- fc import

