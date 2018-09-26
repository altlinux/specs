%define  pkgname friendly_id

Name:    ruby-%pkgname
Version: 5.2.4
Release: alt1

Summary: FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for ActiveRecord.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/norman/friendly_id

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%description
FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for
Active Record. It lets you create pretty URLs and work with human-friendly
strings as if they were numeric ids.

With FriendlyId, it's easy to make your application use URLs like:

    http://example.com/states/washington

instead of:

    http://example.com/states/4323454


%description -l ru_RU.UTF8
FriendlyId есть "Землекоп швейцарской армии", позволяющий выдавать жетоны и постоянные ссылки
для АктивныхЗаписей. Также позволяет создавать красивые ЕРМы (URLs) и работать с человеколюбивыми
строками как если бы они были числами.

С помощью FriendlyId можно легко использовать в вашем приложении ссылки вида:

    http://example.com/states/washington

а не:

    http://example.com/states/4323454

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
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 5.2.4-alt1
- Initial gemified build for Sisyphus
