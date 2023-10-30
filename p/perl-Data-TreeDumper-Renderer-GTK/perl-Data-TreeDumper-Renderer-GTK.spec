%define _unpackaged_files_terminate_build 1
%define m_distro Data-TreeDumper-Renderer-GTK
Name: perl-Data-TreeDumper-Renderer-GTK
Version: 0.03
Release: alt1
Summary: Rendering plug-in for Data::TreeDumper

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~nkh/Data-TreeDumper-Renderer-GTK/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: xvfb-run perl-devel perl-Gtk3 perl-Cairo perl-Data-TreeDumper perl-Term-Size

%description
This Gtk3::TreeView derived widget allows you to diplay a
Data::TreeDumper generated dump in a GTK window. The nodes are
collapsable.

%prep
%setup -q -n %m_distro-%version

%build
%def_without test
%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

# demo
rm -f %buildroot%_bindir/*.pl %buildroot%perl_vendor_privlib/Data/TreeDumper/Renderer/*.pl

%files
%perl_vendor_privlib/Data/TreeDumper/Renderer/GTK*
%perl_vendor_privlib/auto/Data/TreeDumper/Renderer/GTK
%doc Todo README

%changelog
* Mon Oct 30 2023 Igor Vlasenko <viy@altlinux.org> 0.03-alt1
- new version

* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2
- fixed unpackaged files

* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build
