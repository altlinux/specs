Name:    mustache
Version: 1.0.5
Release: alt1

Summary: Logic-less Ruby templates
License: MIT
Group:   Development/Ruby
Url:     https://github.com/mustache/mustache

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -q
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

mkdir -p %buildroot%_man1dir
mv %buildroot%_mandir/*.1 %buildroot%_man1dir
mkdir -p %buildroot%_man5dir
mv %buildroot%_mandir/*.5 %buildroot%_man5dir
rm -f %buildroot%_mandir/*.*

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%_bindir/%name
%ruby_sitelibdir/*
%_man1dir/*.1*
%_man5dir/*.5*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus
