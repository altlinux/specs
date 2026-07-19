%define _unpackaged_files_terminate_build 1
%define module_name GraphViz2

Name: perl-%module_name
Version: 2.67
Release: alt1

Summary: Perl wrapper for AT&T's Graphviz
License: GPL-1.0-or-later OR Artistic-1.0-clause
Group: Development/Perl
URL: %CPAN %module_name
# Source-url: https://cpan.metacpan.org/authors/id/E/ET/ETJ/%module_name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-Data-Section-Simple perl-File-Which perl-Graph perl-IPC-Run3 perl-Moo perl-Type-Tiny perl-Test-Snapshot graphviz fontconfig fonts-ttf-dejavu

Requires: graphviz

%description
GraphViz2 is a Perl wrapper around AT&T's Graphviz tools. It provides an
object-oriented interface for building directed and undirected graphs and
rendering them to various formats using the dot, neato, circo and other
graphviz layout programs.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_privlib/GraphViz2.pm
%perl_vendor_privlib/GraphViz2/

%changelog
* Sun Jul 19 2026 Vitaly Lipatov <lav@altlinux.ru> 2.67-alt1
- initial build for ALT Sisyphus
