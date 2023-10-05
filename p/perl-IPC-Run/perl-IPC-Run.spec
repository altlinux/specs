%define _unpackaged_files_terminate_build 1
%define module IPC-Run
%def_disable test

Name: perl-%module
Version: 20231003.0
Release: alt1

Summary: IPC-Run - system() and background procs w/ piping, redirs, ptys (Unix, Win32)
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/T/TO/TODDR/%{module}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Mar 25 2012
BuildRequires: perl-IO-Tty perl-devel

%description
IPC::Run allows you run and interact with child processes using files, pipes,
and pseudo-ttys. Both system()-style and scripted usages are supported and may
be mixed. Likewise, functional and OO API styles are both supported and may be
mixed.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changelog
%perl_vendor_privlib/IPC/
%exclude %perl_vendor_privlib/IPC/Run/Win*

%changelog
* Thu Oct 05 2023 Igor Vlasenko <viy@altlinux.org> 20231003.0-alt1
- automated CPAN update

* Thu Aug 11 2022 Igor Vlasenko <viy@altlinux.org> 20220807.0-alt1
- automated CPAN update

* Fri Jun 05 2020 Igor Vlasenko <viy@altlinux.ru> 20200505.0-alt1
- automated CPAN update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 20180523.0-alt1
- automated CPAN update

* Sat Mar 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1
- automated CPAN update

* Tue Mar 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.97-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- automated CPAN update

* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 0.91-alt1
- 0.91

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 0.90-alt1
- 0.90

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.89-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 0.89-alt1
- 0.89

* Fri Feb 12 2010 Victor Forsiuk <force@altlinux.org> 0.84-alt1
- 0.84

* Mon Dec 29 2008 Victor Forsyuk <force@altlinux.org> 0.82-alt1
- 0.82

* Tue Oct 03 2006 Victor Forsyuk <force@altlinux.ru> 0.80-alt1
- 0.80
- Exlude Windows specific files from packaging.

* Wed Jun 08 2005 Victor Forsyuk <force@altlinux.ru> 0.79-alt1
- First build for Sisyphus.
