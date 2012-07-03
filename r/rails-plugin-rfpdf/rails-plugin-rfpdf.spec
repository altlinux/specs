# vim: set ft=spec: -*- rpm-spec -*-

%define plugname rfpdf

Name: rails-plugin-rfpdf
Version: 0.2009.07.09
Release: alt1

Summary: RFPDF Template Plugin
License: MIT
Group: Development/Ruby
Url: http://rubyforge.org/projects/rfpdf/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %plugname-%version.tar
Patch: %plugname-%version-%release.patch

PreReq: ruby-railties >= 2.1.0-alt2

# Automatically added by buildreq on Sat Aug 15 2009 (-bi)
BuildRequires: rpm-build-ruby

%description
A template plugin allowing the inclusion of ERB-enabled RFPDF
template files.

%prep
%setup -q -n %plugname-%version
%patch -p1
find lib -type f -exec -print0 |
	xargs -r0 chmod -x --
rm -rf lib/fonts/{dejavu-ttf-2.15,freefont,old,ttf2ufm,ttf-bitstream-vera-1.10}
rm -rf lib/barcode/
rm -rf init.rb lib/rfpdf.rb lib/fpdf/makefont.rb
mv environment.rb init.rb

%build

%install
mkdir -p %buildroot%_datadir/rails/plugins/%plugname
cp -dpR init.rb lib %buildroot%_datadir/rails/plugins/%plugname/

%files
%doc README
%_datadir/rails/plugins/%plugname

%changelog
* Sun Nov 01 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2009.07.09-alt1
- Built for Sisyphus (be451562)

