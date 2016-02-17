# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(Fcntl.pm) perl(IPC/Cmd.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Proc-InvokeEditor
%define upstream_version 1.07

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_5

Summary:    Perl extension for starting a text editor
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Proc/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp/Assert.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: ed
BuildArch:  noarch
Source44: import.info

%description
This module provides the ability to supply some text to an external text
editor, have it edited by the user, and retrieve the results.

The File::Temp module is used to provide secure, safe temporary files, and
File::Temp is set to its highest available level of security. This may
cause problems on some systems where no secure temporary directory is
available.

When the editor is started, no subshell is used. Your path will be scanned
to find the binary to use for each editor if the string given does not
exist as a file, and if a named editor contains whitespace, eg) if you try
to use the editor 'xemacs -nw', then the string will be split on whitespace
and anything after the editor name will be passed as arguments to your
editor. A shell is not used but this should cover most simple cases.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README examples
%perl_vendor_privlib/Proc/


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_5
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_4
- update by mgaimport

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_2
- update by mgaimport

* Fri Aug 29 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1_1
- update by mgaimport

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt3_3
- Sisyphus build

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_3
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 1.06-alt2_2
- rebuild to get rid of unmets

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_1
- converted for ALT Linux by srpmconvert tools

