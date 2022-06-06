%define        gemname RubyInline

Name:          gem-rubyinline
Version:       3.12.5
Release:       alt1
Summary:       Inline allows you to write foreign code within your ruby code
License:       Unlicense
Group:         Development/Ruby
Url:           http://www.zenspider.com/ZSS/Products/RubyInline/
Vcs:           https://github.com/seattlerb/rubyinline.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(ZenTest) >= 4.3 gem(ZenTest) < 5
BuildRequires: gem(hoe) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ZenTest) >= 4.3 gem(ZenTest) < 5
Provides:      gem(RubyInline) = 3.12.5


%description
Inline allows you to write foreign code within your ruby code. It automatically
determines if the code in question has changed and builds it only when
necessary. The extensions are then automatically loaded into the class/module
that defines it.

You can even write extra builders that will allow you to write inlined code in
any language. Use Inline::C as a template and look at Module


%package       -n gem-rubyinline-doc
Version:       3.12.5
Release:       alt1
Summary:       Inline allows you to write foreign code within your ruby code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета RubyInline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(RubyInline) = 3.12.5

%description   -n gem-rubyinline-doc
Inline allows you to write foreign code within your ruby code documentation
files.

Inline allows you to write foreign code within your ruby code. It automatically
determines if the code in question has changed and builds it only when
necessary. The extensions are then automatically loaded into the class/module
that defines it.

You can even write extra builders that will allow you to write inlined code in
any language. Use Inline::C as a template and look at Module

%description   -n gem-rubyinline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета RubyInline.


%package       -n gem-rubyinline-devel
Version:       3.12.5
Release:       alt1
Summary:       Inline allows you to write foreign code within your ruby code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета RubyInline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(RubyInline) = 3.12.5
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 0

%description   -n gem-rubyinline-devel
Inline allows you to write foreign code within your ruby code development
package.

Inline allows you to write foreign code within your ruby code. It automatically
determines if the code in question has changed and builds it only when
necessary. The extensions are then automatically loaded into the class/module
that defines it.

You can even write extra builders that will allow you to write inlined code in
any language. Use Inline::C as a template and look at Module

%description   -n gem-rubyinline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета RubyInline.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.txt
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rubyinline-doc
%doc README.txt
%ruby_gemdocdir

%files         -n gem-rubyinline-devel
%doc README.txt


%changelog
* Sun May 08 2022 Pavel Skrylev <majioa@altlinux.org> 3.12.5-alt1
- + packaged gem with Ruby Policy 2.0
