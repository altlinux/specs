%define        gemname html-proofer

Name:          gem-html-proofer
Version:       5.0.0
Release:       alt1
Summary:       A set of tests to validate your HTML output. These tests check if your image references are legitimate, if they have alt tags, if your internal links are working, and so on. It's intended to be an all-in-one checker for your documentation output
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/gjtorikian/html-proofer
Vcs:           https://github.com/gjtorikian/html-proofer.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(awesome_print) >= 0
BuildRequires: gem(debug) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(rspec) >= 3.1 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(rubocop-standard) >= 0
BuildRequires: gem(timecop) >= 0.8 gem(timecop) < 1
BuildRequires: gem(vcr) >= 2.9 gem(vcr) < 3
BuildRequires: gem(ruby-lsp) >= 0.3.2 gem(ruby-lsp) < 0.4
BuildRequires: gem(addressable) >= 2.3 gem(addressable) < 3
BuildRequires: gem(async) >= 2.1 gem(async) < 3
BuildRequires: gem(nokogiri) >= 1.13 gem(nokogiri) < 2
BuildRequires: gem(rainbow) >= 3.0 gem(rainbow) < 4
BuildRequires: gem(typhoeus) >= 1.3 gem(typhoeus) < 2
BuildRequires: gem(yell) >= 2.0 gem(yell) < 3
BuildRequires: gem(zeitwerk) >= 2.5 gem(zeitwerk) < 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(addressable) >= 2.3 gem(addressable) < 3
Requires:      gem(async) >= 2.1 gem(async) < 3
Requires:      gem(nokogiri) >= 1.13 gem(nokogiri) < 2
Requires:      gem(rainbow) >= 3.0 gem(rainbow) < 4
Requires:      gem(typhoeus) >= 1.3 gem(typhoeus) < 2
Requires:      gem(yell) >= 2.0 gem(yell) < 3
Requires:      gem(zeitwerk) >= 2.5 gem(zeitwerk) < 3
Provides:      gem(html-proofer) = 5.0.0


%description
Test your rendered HTML files to make sure they're accurate.


%package       -n htmlproofer
Version:       5.0.0
Release:       alt1
Summary:       A set of tests to validate your HTML output. These tests check if your image references are legitimate, if they have alt tags, if your internal links are working, and so on. It's intended to be an all-in-one checker for your documentation output executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета html-proofer
Group:         Other
BuildArch:     noarch

Requires:      gem(html-proofer) = 5.0.0

%description   -n htmlproofer
A set of tests to validate your HTML output. These tests check if your image
references are legitimate, if they have alt tags, if your internal links are
working, and so on. It's intended to be an all-in-one checker for your
documentation output executable(s).

Test your rendered HTML files to make sure they're accurate.

%description   -n htmlproofer -l ru_RU.UTF-8
Исполнямка для самоцвета html-proofer.


%package       -n gem-html-proofer-doc
Version:       5.0.0
Release:       alt1
Summary:       A set of tests to validate your HTML output. These tests check if your image references are legitimate, if they have alt tags, if your internal links are working, and so on. It's intended to be an all-in-one checker for your documentation output documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета html-proofer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(html-proofer) = 5.0.0

%description   -n gem-html-proofer-doc
A set of tests to validate your HTML output. These tests check if your image
references are legitimate, if they have alt tags, if your internal links are
working, and so on. It's intended to be an all-in-one checker for your
documentation output documentation files.

Test your rendered HTML files to make sure they're accurate.

%description   -n gem-html-proofer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета html-proofer.


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

%files         -n htmlproofer
%_bindir/htmlproofer

%files         -n gem-html-proofer-doc
%ruby_gemdocdir


%changelog
* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 5.0.0-alt1
- + packaged gem with Ruby Policy 2.0
