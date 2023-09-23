%define plugname syntastic
Name:		vim-plugin-%plugname
Version:	3.10.0
Release:	alt3
Summary:	Syntax checking hacks for vim
Group:		Editors
License:	WTFPL
URL:		https://github.com/vim-syntastic/syntastic
Source:		%name-%version.tar
BuildArch:	noarch

PreReq:		vim-common >= 4:7.0
BuildRequires(pre): rpm-build-vim rpm-build-python3
Packager:	VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%description
             ,
            / \,,_  .'|
         ,{{| /}}}}/_.'          _____________________________________________
        }}}}` '{{'  '.          /                                             \
      {{{{{    _   ;, \        /            Ladies and Gentlemen,              \
   ,}}}}}}    /o`\  ` ;)      |                                                |
  {{{{{{   /           (      |                 this is ...                    |
  }}}}}}   |            \     |                                                |
 {{{{{{{{   \            \    |                                                |
 }}}}}}}}}   '.__      _  |   |    _____             __             __  _      |
 {{{{{{{{       /`._  (_\ /   |   / ___/__  ______  / /_____ ______/ /_(_)____ |
  }}}}}}'      |    //___/ --=:   \__ \/ / / / __ \/ __/ __ `/ ___/ __/ / ___/ |
  `{{{{`       |     '--'     |  ___/ / /_/ / / / / /_/ /_/ (__  ) /_/ / /__   |
   }}}`jgs                    | /____/\__, /_/ /_/\__/\__,_/____/\__/_/\___/   |
                              |      /____/                                    |
                              |                                               /
                               \_____________________________________________/

Syntastic is a syntax checking plugin for Vim created by Martin Grenfell. It
runs files through external syntax checkers and displays any resulting errors
to the user. This can be done on demand, or automatically as files are saved.
If syntax errors are detected, the user is notified and is happy because they
didn't have to compile their code or execute their script to find them.

  Note from upstream: "This project is no longer maintained. If you need a
  syntax checking plugin for Vim you might be interested in Syntastic's
  spiritual succesor, ALE. Although it shares no code with syntastic and it
  takes a very different approach to design, ALE can be considered a natural
  evolution of syntastic in terms of goals and functionality. Check it out, you
  probably won't be disappointed." [2022]

%prep
%setup -q

sed -i 's|#!.*python|&3|' $(find ./ -name '*.py')

%install
mkdir -p %buildroot/%vim_doc_dir
mkdir -p %buildroot/%vim_plugin_dir/syntastic
mkdir -p %buildroot/%vim_autoload_dir/syntastic
install -p -m644 doc/*.txt %buildroot%vim_doc_dir/
install -p -m644 plugin/*.vim %buildroot%vim_plugin_dir/
install -p -m644 plugin/syntastic/*.vim %buildroot%vim_plugin_dir/syntastic/
install -p -m644 autoload/syntastic/*.vim %buildroot%vim_autoload_dir/syntastic/
for i in syntax_checkers/*; do
  mkdir -p %buildroot/%vim_runtime_dir/$i
  install -p -m644 $i/* %buildroot%vim_runtime_dir/$i/
done

%files
%doc LICENCE README.markdown CONTRIBUTING.md
%vim_doc_dir/*
%vim_plugin_dir/*
%vim_autoload_dir/*
%vim_runtime_dir/syntax_checkers/*

%changelog
* Sat Sep 23 2023 Vitaly Chikunov <vt@altlinux.org> 3.10.0-alt3
- Final (upstream) update to 3.10.0-36-g8d5e37c2 (2022-07-10).
- This project is no longer maintained and deprecated in favor of ale.

* Wed Feb 26 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.10.0-alt2
- Porting to python3

* Wed Oct 02 2019 Vitaly Chikunov <vt@altlinux.org> 3.10.0-alt1
- Update to 3.10.0.

* Fri Oct 05 2018 Vitaly Chikunov <vt@altlinux.ru> 3.9.0-alt1
- First package for ALT
