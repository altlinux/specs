%define        gemname glut

Name:          gem-glut
Version:       8.3.0
Release:       alt1
Summary:       Glut bindings for OpenGL
License:       Unlicense
Group:         Development/Ruby
Url:           https://rubygems.org/gems/glut
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc) >= 4.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(glut) = 8.3.0


%description
Glut bindings for OpenGL. To be used with the
{opengl}[https://github.com/larskanis/opengl] gem.


%package       -n gem-glut-doc
Version:       8.3.0
Release:       alt1
Summary:       Glut bindings for OpenGL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета glut
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(glut) = 8.3.0

%description   -n gem-glut-doc
Glut bindings for OpenGL documentation files.

Glut bindings for OpenGL. To be used with the
{opengl}[https://github.com/larskanis/opengl] gem.

%description   -n gem-glut-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета glut.


%package       -n gem-glut-devel
Version:       8.3.0
Release:       alt1
Summary:       Glut bindings for OpenGL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета glut
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(glut) = 8.3.0
Requires:      gem(rdoc) >= 4.0

%description   -n gem-glut-devel
Glut bindings for OpenGL development package.

Glut bindings for OpenGL. To be used with the
{opengl}[https://github.com/larskanis/opengl] gem.

%description   -n gem-glut-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета glut.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-glut-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-glut-devel
%doc README.rdoc
%ruby_includedir/*


%changelog
* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 8.3.0-alt1
- + packaged gem with Ruby Policy 2.0
