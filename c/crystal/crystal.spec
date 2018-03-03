# To bootstrap toggle bootstrap knob (change def_disable to def_enable) and
# add to git crystal compiler with name crystal-bin-alt
%def_disable bootstrap

Name:     crystal
Version:  0.24.1
Release:  alt1.163c0cb0cc.2

Summary:  The Crystal Programming Language
License:  Apache-2.0
Group:    Development/Other
Url:      https://github.com/crystal-lang/crystal

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source0:  %name-%version.tar
%if_enabled bootstrap
Source1:  crystal-bin-alt
%endif
Source2:  crystal-starter-alt
Patch0:   crystal-0.24.1-alt-make.patch
Patch1:   crystal-0.24.1-alt-errno-appropriate-interface.patch

%if_disabled bootstrap
BuildRequires:  crystal
%endif
BuildRequires: llvm4.0-devel gcc-c++
BuildRequires: libevent-devel zlib-devel libgc-devel libpcre-devel libssl-devel libyaml-devel
BuildRequires: /proc

ExclusiveArch: x86_64

%description
Crystal is a programming language with the following goals:

Have a syntax similar to Ruby (but compatibility with it is not a goal)
Statically type-checked but without having to specify the type of variablesor
method arguments.  Be able to call C code by writing bindings to it in Crystal.
Have compile-time evaluation and generation of code, to avoid boilerplate code.
Compile to efficient native code.


%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%if_enabled bootstrap
mkdir -p ALT/bin
cp %SOURCE1 -T ALT/bin/crystal
export PATH="$PATH:ALT/bin"
%endif
%make_build release=1 progress=true CRYSTAL_CONFIG_PATH="lib:/usr/lib/crystal" CRYSTAL_PATH=/usr/lib/crystal/src/

%install
install -D %SOURCE2 -T %buildroot%_bindir/%name
install -D .build/%name -t %buildroot%_libexecdir/%name/bin
cp -r src %buildroot%_libexecdir/%name
xz man/%name.1
install -D man/%name.1.xz -t %buildroot%_man1dir
install -D etc/completion.zsh %buildroot%_datadir/zsh/site-functions/_%name

%files
%_bindir/%name
%_libexecdir/%name
%doc %_man1dir/*
%_datadir/zsh/site-functions/_%name

%changelog
* Sat Mar 03 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.24.1-alt1.163c0cb0cc.2
- Disable bootstrap knob

* Sat Mar 03 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.24.1-alt1.163c0cb0cc.1
- Initial build for Sisyphus
