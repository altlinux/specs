%define module DIME-Tools
%define m_distro DIME-Tools
%define m_name DIME::Tools
%define m_author_id unknown
%def_disable test

Name: perl-DIME-Tools
Version: 0.03
Release: alt3.1

Summary: modules for parsing and generate DIME messages

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Afanasov Dmitry <ender@altlinux.org>

BuildArch: noarch
Source: %m_distro-%version.tar

# Automatically added by buildreq on Mon Jun 26 2006
BuildRequires: perl-devel
BuildRequires: perl-Data-UUID perl-IO-stringy

%description
DIME-tools is a collection of DIME:: modules for parse and generate DIME
encoded messages ( Direct Internet Message Encapsulation ). DIME-tools support
single-record and chunked payloads for sending big attachments.

%prep
%setup -q -n %m_distro-%version
find . -name '*.pm' -print0  | xargs -r0 subst "s,\r,," 
%build
%perl_vendor_build

%install
%perl_vendor_install
#add_findreq_skiplist */DIME/Identifier.pm

%files
%perl_vendor_privlib/DIME

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Dec 08 2008 Afanasov Dmitry <ender@altlinux.org> 0.03-alt3
- fix requires on UUID (must be DATA::UUID)
- dirty tarball is packed :(

* Sun Dec 07 2008 Afanasov Dmitry <ender@altlinux.org> 0.03-alt2
- fix build (remove i386-linux from %files)

* Mon Jun 26 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.03-alt1
- first build for ALT Linux Sisyphus

