%define  pkgname deacon

Name:    ruby-%pkgname
Version: 1.0.0
Release: alt1

Summary: Human readable name generator plugin
License: GPL-3.0
Group:   Development/Ruby
Url:     https://github.com/lzap/deacon

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

Patch1: fix-data-share-dir.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
Out of ideas for incoming bare-metal host names in your cluster? This little gem
is a way out! It contains frequently occurring given names and surnames from the
1990 US Census (public domain data):

 * 256 (8 bits) unique male given names
 * 256 (8 bits) unique female given names
 * 65,536 (16 bits) unique surnames

Given names were filtered to be 3-5 characters long, surnames 5-8 characters,
therefore generated names are never longer than 14 characters (5+1+8).

This gives 33,554,432 (25 bits) total of male and female name combinations.
Built-in generator can either generate randomized succession, or generate
combinations based on MAC adresses.

%description -l ru_RU.UTF8
Модель генератора человекочитаемых имён

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%description doc -l ru_RU.UTF8
Файлы сведений для %name

%prep
%setup -n %pkgname-%version
%patch1 -p 1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
mkdir -p %buildroot%_datadir/%name
mv %buildroot/%_datadir/*.txt %buildroot/%_datadir/%name

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*
%_datadir/%name/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial gemified build for Sisyphus
