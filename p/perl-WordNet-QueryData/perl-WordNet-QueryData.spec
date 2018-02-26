%define module_name WordNet-QueryData

Name: perl-%module_name
Version: 1.49
Release: alt2

Summary: Perl interface to the WordNet database
License: Perl
Group: Development/Perl
Url: http://people.csail.mit.edu/jrennie/WordNet
BuildArch: noarch
# http://people.csail.mit.edu/jrennie/WordNet/WordNet-QueryData-1.49.tar.gz
Source: %module_name-%version.tar
Requires: wordnet-dict-sense-index
BuildRequires: perl-devel wordnet-dict

%description
WordNet::QueryData provides a direct interface to the WordNet database
files.

%prep
%setup -n %module_name-%version

%build
export WNHOME=/usr/share/wordnet
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README test.pl
%perl_vendorlib/WordNet/

%changelog
* Mon Nov 15 2010 Dmitry V. Levin <ldv@altlinux.org> 1.49-alt2
- Fixed build with new perl.

* Thu Oct 29 2009 Dmitry V. Levin <ldv@altlinux.org> 1.49-alt1
- Updated to 1.49.

* Fri Mar 06 2009 Vyacheslav Dikonov <slava@altlinux.ru> 1.47-alt1
- ALTLinux build
