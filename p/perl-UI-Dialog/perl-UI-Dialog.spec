%define _unpackaged_files_terminate_build 1
%filter_from_requires /^perl.UI.Dialog.Backend.NotifySend.pm./d
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Config.pm) perl(FileHandle.pm) perl(File/Slurp.pm) perl(Gnome2/GConf.pm) perl(Test/More.pm) perl(Time/HiRes.pm) perl(diagnostics.pm) perl(String/ShellQuote.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%filter_from_requires /^perl.Gnome2.GConf.pm/d
%define upstream_name    UI-Dialog
%define upstream_version 1.20

Name:       perl-%{upstream_name}
Version:    1.20
Release:    alt1

Summary:    OOPerl wrapper for the various dialog applications
License:    GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/K/KC/KCK/UI-Dialog-%{version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Text/Wrap.pm)
BuildArch:  noarch

Requires:   perl
Requires:   cdialog
Source44: import.info
%description
UI::Dialog is a OOPerl wrapper for the various dialog applications. These
dialog backends are currently supported: Zenity, GDialog, XDialog, KDialog,
CDialog, and Whiptail. There is also an ASCII backend provided as a last
resort interface for the console based dialog variants. UI::Dialog is a
class that provides a strict interface to these various backend modules.
By using UI:Dialog (with it's imposed limitations on the widgets) you can
ensure that your Perl program will function with any available interfaces.

UI::Dialog supports priority ordering of the backend detection process. So
if you'd prefer that Xdialog should be used first if available, simply
designate the desired order when creating the new object. The default order
for detecting and utilization of the backends are as follows:
  (with DISPLAY env): Zenity, GDialog, XDialog, KDialog
  (without DISPLAY): CDialog, Whiptail, ASCII

UI::Dialog is the result of a complete re-write of the UDPM CPAN module. This
was done to break away from the bad choice of name (UserDialogPerlModule) and
to implement a cleaner, more detached, OOPerl interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make

%check
# disabled as some backend utils are not present
#make test

%install
%makeinstall_std

%files
%doc CONTRIBUTORS Changes README TODO examples
%{perl_vendor_privlib}/*

%changelog
* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Fri Nov 13 2015 Igor Vlasenko <viy@altlinux.ru> 1.09_2-alt1
- automated CPAN update

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 1.09-alt3_4
- to Sisyphus

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.09-alt2_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.09-alt2_2
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1.09-alt2_1
- rebuild to get rid of unmets

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1_1
- update by mgaimport

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_4
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_3
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_2
- converted for ALT Linux by srpmconvert tools

