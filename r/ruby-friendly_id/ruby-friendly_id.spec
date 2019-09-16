%define        pkgname friendly_id
%define        gemname friendly_id

Name:          ruby-%pkgname
Version:       5.2.5
Release:       alt1
Summary:       FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for ActiveRecord.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/norman/friendly_id
%vcs           https://github.com/norman/friendly_id.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

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

%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.5-alt1
- ^ v5.2.5
- ^ Ruby Policy 2.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 5.2.4-alt1
- Initial gemified build for Sisyphus
