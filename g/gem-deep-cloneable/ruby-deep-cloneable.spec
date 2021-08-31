%define        gemname deep_cloneable

Name:          gem-deep-cloneable
Version:       3.1.0
Release:       alt1
Summary:       Gives every ActiveRecord::Base object the possibility to do a deep clone
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/moiristo/deep_cloneable
Vcs:           https://github.com/moiristo/deep_cloneable.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activerecord) >= 3.1.0 gem(activerecord) < 7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activerecord) >= 3.1.0 gem(activerecord) < 7
Obsoletes:     ruby-deep-cloneable < %EVR
Provides:      ruby-deep-cloneable = %EVR
Provides:      gem(deep_cloneable) = 3.1.0


%description
This gem gives every ActiveRecord::Base object the possibility to do a deep
clone that includes user specified associations. It is a rails 3+ upgrade of the
deep_cloning plugin.


%package       -n gem-deep-cloneable-doc
Version:       3.1.0
Release:       alt1
Summary:       Gives every ActiveRecord::Base object the possibility to do a deep clone documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета deep_cloneable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(deep_cloneable) = 3.1.0

%description   -n gem-deep-cloneable-doc
Gives every ActiveRecord::Base object the possibility to do a deep clone
documentation files.

This gem gives every ActiveRecord::Base object the possibility to do a deep
clone that includes user specified associations. It is a rails 3+ upgrade of the
deep_cloning plugin.

%description   -n gem-deep-cloneable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета deep_cloneable.


%package       -n gem-deep-cloneable-devel
Version:       3.1.0
Release:       alt1
Summary:       Gives every ActiveRecord::Base object the possibility to do a deep clone development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета deep_cloneable
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(deep_cloneable) = 3.1.0

%description   -n gem-deep-cloneable-devel
Gives every ActiveRecord::Base object the possibility to do a deep clone
development package.

This gem gives every ActiveRecord::Base object the possibility to do a deep
clone that includes user specified associations. It is a rails 3+ upgrade of the
deep_cloning plugin.

%description   -n gem-deep-cloneable-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета deep_cloneable.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-deep-cloneable-doc
%ruby_gemdocdir

%files         -n gem-deep-cloneable-devel


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 3.0.0 -> 3.1.0

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- used (>) Ruby Policy 2.0
- updated (^) 2.3.2 -> 3.0.0

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt1
- Initial build for Sisyphus
