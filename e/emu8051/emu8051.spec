Name: emu8051
Version: 0.71
Release: alt1
License: MIT
Group: Emulators
BuildPreReq: libncurses-devel gcc-c++
Source0: %name.tar
Summary: 8051 emulator
%description
This is a simulator of the 8051/8052 microcontrollers. For sake of simplicity, 
I'm only referring to 8051, although the emulator can emulate either one. For 
more information about the 8-bit chip(s), please check out www.8052.com or look 
up the data sheets. Intel, being the originator of the architecture, naturally 
has information as well.

The 8051 is a pretty easy chip to play with, in both hardware and software. 
Hence, it's a good chip to use as an example when teaching about computer hardware. 
Unfortunately, the simulators in use in my school were a bit outdated, so I 
decided to write a new one.

The scope of the emulator is to help test and debug 8051 assembler programs. 
What is particularily left out is clock-cycle exact simulation of processor 
pins. (For instance, MUL is a 48-clock operation on the 8051. On which 
clock cycle does the CPU read the operands? Or write the result?). Such 
simulation might help in designing some hardware, but for most uses it is 
unneccessary and complicated.

The emulator is designed to have two separate modules, consisting of the emulator 
core and separate front-end. This enables the creation of different kinds of 
front-ends. For instance, this lets the user use the emulator core as a DLL in 
a C/C++ application which can simulate other kinds of hardware (such as leds, 
switches, displays, audio, or whatnot).

Simulation accuracy is valued over speed. Nevertheless, already at v.0.1 the 
emulator could run at over-realtime speeds on a P4/2.6GHz (running the emulator 
at over 12MHz). Based on profiler output, over half of the processing time is 
wasted on pipeline trashing when branching to the opcode functions. This could 
possibly be helped by JITing the code, but that is considered unneccessary at 
this point. Also, CPUs with shorter pipelines are not harmed by this behavior as badly.

The emulator is written completely in ANSI C for portability, and the sources 
are available under the MIT license.

Current features include:

    * Full 8051 instruction set.
    * ncurses-based UI - works fine over SSH for instance.
      The main view includes:
          o Memory view.
          o Stack view.
          o Opcode and disassembly view.
          o History view of SP, P0, P1, P2, P3, IP, IE, TMOD, TCON, TH0, TL0, TH1, TL1, SCON, PCON, A, B, R0, R1, R2, R3, R4, R5, R6, R7 and DPTR, as well as all processor status bits.
          o Cycle and real-time counter.
      Other views include:
          o Logic board (leds'n'switches) view, with optional widgets such as 7-seg displays and 44780-style text output
          o Memory editor, showing all five types of memory at the same time
          o Options, where user can disable debug exceptions etc.
    * Support for all sorts of 8051 memory combinations - 128 or 256B internal RAM, 0-64k of external RAM and 0-64k of ROM. External RAM and ROM may even point at the same memory, enabling self-modifying code.
    * Loads Intel HEX files.
    * Support for exceptions on invalid instructions, odd stack behavior, and messing up important registers in interrupts. One breakpoint is also supported.
    * The emulator performs callbacks on register area or external memory read/write, which can be used to implement simulation of new special features or whatever is connected to the IO ports.
    * Timer 0 and 1 modes 0, 1, 2 and 3, as well as interrupt priorities.

%prep
%setup -q -n %name
%build
bash build.sh
%install 
bash install.sh %buildroot
%files
/usr/bin/emu8051
%_datadir/doc/%name-%version


%changelog
* Sat Jan 05 2008 Yury A. Romanov <damned@altlinux.ru> 0.71-alt1
- Initial build
- Added spec file and scripts for building/installing


