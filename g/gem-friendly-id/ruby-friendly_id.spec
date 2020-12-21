%define        pkgname friendly-id
%define        gemname friendly_id

Name:          gem-%pkgname
Version:       5.4.1
Release:       alt1
Summary:       FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for ActiveRecord.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/norman/friendly_id
Vcs:           https://github.com/norman/friendly_id.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
FriendlyId is the "Swiss Army bulldozer" of slugging and permalink plugins for
Active Record. It lets you create pretty URLs and work with human-friendly
strings as if they were numeric ids.

With FriendlyId, it's easy to make your application use URLs like:

    http://example.com/states/washington

instead of:

    http://example.com/states/4323454


%description -l ru_RU.UTF8
FriendlyId есть "Землекоп швейцарской армии", позволяющий выдавать жетоны и
постоянные ссылки для АктивныхЗаписей. Также позволяет создавать красивые ЕРМы
(URLs) и работать с дружественными человеку строками как если бы они были
числами.

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
* Mon Dec 21 2020 Pavel Skrylev <majioa@altlinux.org> 5.4.1-alt1
- ^ 5.3.0 -> 5.4.1
- ! spec

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 5.3.0-alt1
- ^ 5.2.5 -> 5.3.0
- * policify name

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.5-alt1
- > Ruby Policy 2.0
- ^ 5.2.4 -> 5.2.5

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 5.2.4-alt1
- Initial gemified build for Sisyphus
