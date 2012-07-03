%define m_distro Data-TreeDumper-Renderer-GTK
Name: perl-Data-TreeDumper-Renderer-GTK
Version: 0.02
Release: alt1
Summary: Rendering plug-in for Data::TreeDumper

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~nkh/Data-TreeDumper-Renderer-GTK/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: xvfb-run perl-devel perl-Gtk2 perl-Cairo perl-Data-TreeDumper perl-Term-Size

%description
This Gtk2::TreeView derived widget allows you to diplay a
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

%files
%perl_vendor_privlib/Data/TreeDumper/Renderer/GTK*
%perl_vendor_privlib/auto/Data/TreeDumper/Renderer/GTK
%doc Changes Todo README 

%changelog
* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build
