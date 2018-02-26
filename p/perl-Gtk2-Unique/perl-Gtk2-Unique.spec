%define dist Gtk2-Unique

Name: perl-%dist
Version: 0.05
Release: alt1.1

Summary: Use single instance applications
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: http://search.cpan.org/CPAN/authors/id/P/PO/POTYL/Gtk2-Unique-%version.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: libunique-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Gtk2-devel perl-podlators xvfb-run

%description
Perl bindings for the C library "libunique" that provides a mechanism
for writing single instance applications. If you launch a single
instance application twice, the second instance will either just quit or
will send a message to the running instance.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

%files
%doc	Changes README examples
%dir	%perl_vendor_archlib/Gtk2
	%perl_vendor_archlib/Gtk2/Unique.pm
%doc	%perl_vendor_archlib/Gtk2/Unique*.pod
	%perl_vendor_autolib/Gtk2
# XXX devel?
%dir	%perl_vendor_archlib/Gtk2/Unique
%doc	%perl_vendor_archlib/Gtk2/Unique/*.pod
	%perl_vendor_archlib/Gtk2/Unique/Install

%changelog
* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt1.1
- rebuilt for pelr-5.14

* Wed Feb 09 2011 Victor Forsiuk <force@altlinux.org> 0.05-alt1
- Initial build.
