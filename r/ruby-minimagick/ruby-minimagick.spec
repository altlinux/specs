%define  pkgname minimagick

Name:    ruby-%pkgname
Version: 4.8.0
Release: alt1

Summary: mini replacement for RMagick
License: MIT
Group:   Development/Ruby
Url:     https://github.com/minimagick/minimagick

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

Requires: ImageMagick-tools

%description
Using MiniMagick the ruby processes memory remains small (it spawns
ImageMagick's command line program mogrify which takes up some memory as
well, but is much smaller compared to RMagick).

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.0-alt1
- Initial build for Sisyphus
