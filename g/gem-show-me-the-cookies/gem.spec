%define        gemname show_me_the_cookies

Name:          gem-show-me-the-cookies
Version:       5.0.1
Release:       alt1
Summary:       Cookie manipulation for Capybara drivers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/nruth/show_me_the_cookies
Vcs:           https://github.com/nruth/show_me_the_cookies.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(capybara) >= 2 gem(capybara) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(capybara) >= 2 gem(capybara) < 4
Provides:      gem(show_me_the_cookies) = 5.0.1


%description
Cookie manipulation for Capybara drivers -- viewing, deleting, ...


%package       -n gem-show-me-the-cookies-doc
Version:       5.0.1
Release:       alt1
Summary:       Cookie manipulation for Capybara drivers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета show_me_the_cookies
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(show_me_the_cookies) = 5.0.1

%description   -n gem-show-me-the-cookies-doc
Cookie manipulation for Capybara drivers documentation files.

Cookie manipulation for Capybara drivers -- viewing, deleting, ...

%description   -n gem-show-me-the-cookies-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета show_me_the_cookies.


%package       -n gem-show-me-the-cookies-devel
Version:       5.0.1
Release:       alt1
Summary:       Cookie manipulation for Capybara drivers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета show_me_the_cookies
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(show_me_the_cookies) = 5.0.1

%description   -n gem-show-me-the-cookies-devel
Cookie manipulation for Capybara drivers development package.

Cookie manipulation for Capybara drivers -- viewing, deleting, ...

%description   -n gem-show-me-the-cookies-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета show_me_the_cookies.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-show-me-the-cookies-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-show-me-the-cookies-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 5.0.1-alt1
- + packaged gem with Ruby Policy 2.0
