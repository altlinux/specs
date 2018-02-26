Name: pyclewn
Version: 1.9
Release: alt1
License: GPLv2
Summary: Using vim as a front end to a debugger (supports gdb and pdb)
Group: Development/Debuggers
BuildPreReq: rpm-build-vim
BuildArch: noarch
Source: %name-%version.py2.tar.gz

# Automatically added by buildreq on Wed May 02 2012
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-logging
BuildRequires: python-devel vim-console
%add_python_req_skip msvcrt win32con win32console win32gui win32pipe

%description
Pyclewn allows using vim as a front end to a debugger. Pyclewn currently
supports gdb and pdb.

The debugger output is redirected to a vim window, the pyclewn console.
The debugger commands are mapped to vim user-defined commands with
a common letter prefix, and with completion available on the commands
and their first argument.

On unix when running gvim, the controlling terminal of the program to
debug is the terminal used to launch pyclewn. Any other terminal can be
used when the debugger allows it, for example after using the attach or
tty gdb commands or using the --tty option with pdb. On Windows, gdb
pops up a console attached to the program to debug.

%setup_python_module %name
%package -n %packagename
Group: Development/Python
Summary: Supplemental module for %name
%description -n %packagename
Supplemental module for %name

%prep
%setup -n %name-%version.py2

%build
export EDITOR=/usr/bin/vim
%python_build

%install
export EDITOR=/usr/bin/vim
%python_install

%files
%doc README
%vim_runtime_dir/*/*
%vim_runtime_dir/*/.??*
%_bindir/*

%files -n %packagename
%python_sitelibdir_noarch/*

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 1.9-alt1
- Autobuild version bump to 1.9

* Thu May 03 2012 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Initial build from scratch

