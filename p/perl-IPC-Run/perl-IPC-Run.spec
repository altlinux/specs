%define module IPC-Run
%def_disable test

Name: perl-%module
Version: 0.91
Release: alt1

Summary: IPC-Run - system() and background procs w/ piping, redirs, ptys (Unix, Win32)
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/IPC-Run-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Mar 25 2012
BuildRequires: perl-IO-Tty perl-devel

%description
IPC::Run allows you run and interact with child processes using files, pipes,
and pseudo-ttys. Both system()-style and scripted usages are supported and may
be mixed. Likewise, functional and OO API styles are both supported and may be
mixed.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/IPC/
%exclude %perl_vendor_privlib/IPC/Run/Win*

%changelog
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
