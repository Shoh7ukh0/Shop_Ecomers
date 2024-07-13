# typed: true

# DO NOT EDIT MANUALLY
# This is an autogenerated file for types exported from the `patchelf` gem.
# Please instead update this file by running `bin/tapioca gem patchelf`.

# Main module of patchelf.
#
# @author david942j
#
# source://patchelf//lib/patchelf.rb#6
module PatchELF; end

# Helper methods for internal usage.
#
# source://patchelf//lib/patchelf/helper.rb#5
module PatchELF::Helper
  private

  # @example
  #   aligndown(0x1234)
  #   #=> 4096
  #   aligndown(0x33, 0x20)
  #   #=> 32
  #   aligndown(0x10, 0x8)
  #   #=> 16
  # @param val [Integer]
  # @param align [Integer]
  # @return [Integer] Aligned result.
  #
  # source://patchelf//lib/patchelf/helper.rb#65
  def aligndown(val, align = T.unsafe(nil)); end

  # @example
  #   alignup(0x1234)
  #   #=> 8192
  #   alignup(0x33, 0x20)
  #   #=> 64
  #   alignup(0x10, 0x8)
  #   #=> 16
  # @param val [Integer]
  # @param align [Integer]
  # @return [Integer] Aligned result.
  #
  # source://patchelf//lib/patchelf/helper.rb#80
  def alignup(val, align = T.unsafe(nil)); end

  # For {#colorize} to decide if need add color codes.
  #
  # @return [Boolean]
  #
  # source://patchelf//lib/patchelf/helper.rb#50
  def color_enabled?; end

  # For wrapping string with color codes for prettier inspect.
  #
  # @param str [String] Content to colorize.
  # @param type [Symbol] Specify which kind of color to use, valid symbols are defined in {.COLOR_CODE}.
  # @return [String] String that wrapped with color codes.
  #
  # source://patchelf//lib/patchelf/helper.rb#40
  def colorize(str, type); end

  # The size of one page.
  #
  # source://patchelf//lib/patchelf/helper.rb#17
  def page_size(e_machine = T.unsafe(nil)); end

  class << self
    # @example
    #   aligndown(0x1234)
    #   #=> 4096
    #   aligndown(0x33, 0x20)
    #   #=> 32
    #   aligndown(0x10, 0x8)
    #   #=> 16
    # @param val [Integer]
    # @param align [Integer]
    # @return [Integer] Aligned result.
    #
    # source://patchelf//lib/patchelf/helper.rb#65
    def aligndown(val, align = T.unsafe(nil)); end

    # @example
    #   alignup(0x1234)
    #   #=> 8192
    #   alignup(0x33, 0x20)
    #   #=> 64
    #   alignup(0x10, 0x8)
    #   #=> 16
    # @param val [Integer]
    # @param align [Integer]
    # @return [Integer] Aligned result.
    #
    # source://patchelf//lib/patchelf/helper.rb#80
    def alignup(val, align = T.unsafe(nil)); end

    # For {#colorize} to decide if need add color codes.
    #
    # @return [Boolean]
    #
    # source://patchelf//lib/patchelf/helper.rb#50
    def color_enabled?; end

    # For wrapping string with color codes for prettier inspect.
    #
    # @param str [String] Content to colorize.
    # @param type [Symbol] Specify which kind of color to use, valid symbols are defined in {.COLOR_CODE}.
    # @return [String] String that wrapped with color codes.
    #
    # source://patchelf//lib/patchelf/helper.rb#40
    def colorize(str, type); end

    # The size of one page.
    #
    # source://patchelf//lib/patchelf/helper.rb#17
    def page_size(e_machine = T.unsafe(nil)); end
  end
end

# Color codes for pretty print.
#
# source://patchelf//lib/patchelf/helper.rb#9
PatchELF::Helper::COLOR_CODE = T.let(T.unsafe(nil), Hash)

# A logger for internal usage.
#
# source://patchelf//lib/patchelf/logger.rb#9
module PatchELF::Logger
  private

  # source://patchelf//lib/patchelf/logger.rb#19
  def debug(msg); end

  # source://patchelf//lib/patchelf/logger.rb#19
  def error(msg); end

  # source://patchelf//lib/patchelf/logger.rb#19
  def info(msg); end

  # source://patchelf//lib/patchelf/logger.rb#19
  def level=(msg); end

  # source://patchelf//lib/patchelf/logger.rb#19
  def warn(msg); end

  class << self
    # source://patchelf//lib/patchelf/logger.rb#19
    def debug(msg); end

    # source://patchelf//lib/patchelf/logger.rb#19
    def error(msg); end

    # source://patchelf//lib/patchelf/logger.rb#19
    def info(msg); end

    # source://patchelf//lib/patchelf/logger.rb#19
    def level=(msg); end

    # source://patchelf//lib/patchelf/logger.rb#19
    def warn(msg); end
  end
end

# Memory management, provides malloc/free to allocate LOAD segments.
#
# @private
#
# source://patchelf//lib/patchelf/mm.rb#8
class PatchELF::MM
  # Instantiate a {MM} object.
  #
  # @param elf [ELFTools::ELFFile]
  # @return [MM] a new instance of MM
  #
  # source://patchelf//lib/patchelf/mm.rb#14
  def initialize(elf); end

  # Let the malloc / free requests be effective.
  #
  # @return [void]
  #
  # source://patchelf//lib/patchelf/mm.rb#35
  def dispatch!; end

  # @return [Integer] The size extended.
  #
  # source://patchelf//lib/patchelf/mm.rb#9
  def extend_size; end

  # Query if extended.
  #
  # @return [Boolean]
  #
  # source://patchelf//lib/patchelf/mm.rb#57
  def extended?; end

  # Get correct offset after the extension.
  #
  # @param off [Integer]
  # @return [Integer] Shifted offset.
  #
  # source://patchelf//lib/patchelf/mm.rb#66
  def extended_offset(off); end

  # @param size [Integer]
  # @raise [ArgumentError]
  # @return [void]
  # @yieldparam off [Integer]
  # @yieldparam vaddr [Integer]
  # @yieldreturn [void] One can only do the following things in the block:
  #   1. Set ELF headers' attributes (with ELFTools)
  #   2. Invoke {Saver#inline_patch}
  #
  # source://patchelf//lib/patchelf/mm.rb#27
  def malloc(size, &block); end

  # @return [Integer] Where the file start to be extended.
  #
  # source://patchelf//lib/patchelf/mm.rb#10
  def threshold; end

  private

  # @raise [ArgumentError]
  #
  # source://patchelf//lib/patchelf/mm.rb#182
  def abnormal_elf(msg); end

  # source://patchelf//lib/patchelf/mm.rb#86
  def extend_backward(seg, size = T.unsafe(nil)); end

  # source://patchelf//lib/patchelf/mm.rb#93
  def extend_forward(seg, size = T.unsafe(nil)); end

  # source://patchelf//lib/patchelf/mm.rb#75
  def fgap_method; end

  # source://patchelf//lib/patchelf/mm.rb#122
  def find_gap(check_sz: T.unsafe(nil)); end

  # source://patchelf//lib/patchelf/mm.rb#174
  def invoke_callbacks(seg, start); end

  # source://patchelf//lib/patchelf/mm.rb#170
  def load_segments; end

  # source://patchelf//lib/patchelf/mm.rb#102
  def mgap_method; end

  # TODO
  #
  # @raise [NotImplementedError]
  #
  # source://patchelf//lib/patchelf/mm.rb#138
  def new_load_method; end

  # For all attributes >= threshold, += offset
  #
  # source://patchelf//lib/patchelf/mm.rb#147
  def shift_attributes; end

  # @return [Boolean]
  #
  # source://patchelf//lib/patchelf/mm.rb#142
  def writable?(seg); end
end

# Raised on missing Program Header(segment)
#
# source://patchelf//lib/patchelf/exceptions.rb#14
class PatchELF::MissingSegmentError < ::PatchELF::PatchError; end

# Raised when Dynamic Tag is missing
#
# source://patchelf//lib/patchelf/exceptions.rb#11
class PatchELF::MissingTagError < ::PatchELF::PatchError; end

# Raised on an error during ELF modification.
#
# source://patchelf//lib/patchelf/exceptions.rb#8
class PatchELF::PatchError < ::ELFTools::ELFError; end

# Class to handle all patching things.
#
# source://patchelf//lib/patchelf/patcher.rb#12
class PatchELF::Patcher
  # Instantiate a {Patcher} object.
  #
  # @param filename [String] Filename of input ELF.
  # @param logging [Boolean] *deprecated*: use +on_error+ instead
  # @param on_error [:log, :silent, :exception] action when the desired segment/tag field isn't present
  #   :log = logs to stderr
  #   :exception = raise exception related to the error
  #   :silent = ignore the errors
  # @raise [ArgumentError]
  # @return [Patcher] a new instance of Patcher
  #
  # source://patchelf//lib/patchelf/patcher.rb#28
  def initialize(filename, on_error: T.unsafe(nil), logging: T.unsafe(nil)); end

  # Add the needed library.
  #
  # @note This setting will be saved after {#save} being invoked.
  # @param need [String]
  # @return [void]
  #
  # source://patchelf//lib/patchelf/patcher.rb#81
  def add_needed(need); end

  # @note This setting will be saved after {#save} being invoked.
  #
  # source://patchelf//lib/patchelf/patcher.rb#16
  def elf; end

  # @example
  #   PatchELF::Patcher.new('/bin/ls').interpreter
  #   #=> "/lib64/ld-linux-x86-64.so.2"
  # @return [String?] Get interpreter's name.
  #
  # source://patchelf//lib/patchelf/patcher.rb#44
  def interpreter; end

  # Set interpreter's name.
  #
  # If the input ELF has no existent interpreter,
  # this method will show a warning and has no effect.
  #
  # @note This setting will be saved after {#save} being invoked.
  # @param interp [String]
  #
  # source://patchelf//lib/patchelf/patcher.rb#54
  def interpreter=(interp); end

  # Get needed libraries.
  #
  # @example
  #   patcher = PatchELF::Patcher.new('/bin/ls')
  #   patcher.needed
  #   #=> ["libselinux.so.1", "libc.so.6"]
  # @return [Array<String>]
  #
  # source://patchelf//lib/patchelf/patcher.rb#66
  def needed; end

  # Set needed libraries.
  #
  # @note This setting will be saved after {#save} being invoked.
  # @param needs [Array<String>]
  #
  # source://patchelf//lib/patchelf/patcher.rb#73
  def needed=(needs); end

  # Remove the needed library.
  #
  # @note This setting will be saved after {#save} being invoked.
  # @param need [String]
  # @return [void]
  #
  # source://patchelf//lib/patchelf/patcher.rb#90
  def remove_needed(need); end

  # Replace needed library +src+ with +tar+.
  #
  # @note This setting will be saved after {#save} being invoked.
  # @param src [String] Library to be replaced.
  # @param tar [String] Library replace with.
  # @return [void]
  #
  # source://patchelf//lib/patchelf/patcher.rb#103
  def replace_needed(src, tar); end

  # Get rpath
  # return [String?]
  #
  # source://patchelf//lib/patchelf/patcher.rb#142
  def rpath; end

  # Set rpath
  #
  # Modify / set DT_RPATH of the given ELF.
  # similar to runpath= except DT_RPATH is modifed/created in DYNAMIC segment.
  #
  # @note This setting will be saved after {#save} being invoked.
  # @param rpath [String]
  #
  # source://patchelf//lib/patchelf/patcher.rb#152
  def rpath=(rpath); end

  # Get runpath.
  #
  # @return [String?]
  #
  # source://patchelf//lib/patchelf/patcher.rb#136
  def runpath; end

  # Set runpath.
  #
  # If DT_RUNPATH is not presented in the input ELF,
  # a new DT_RUNPATH attribute will be inserted into the DYNAMIC segment.
  #
  # @note This setting will be saved after {#save} being invoked.
  # @param runpath [String]
  #
  # source://patchelf//lib/patchelf/patcher.rb#162
  def runpath=(runpath); end

  # Save the patched ELF as +out_file+.
  #
  # @param out_file [String?] If +out_file+ is +nil+, the original input file will be modified.
  # @param patchelf_compatible [Boolean] When +patchelf_compatible+ is true, tries to produce same ELF as the one produced by NixOS/patchelf.
  # @return [void]
  #
  # source://patchelf//lib/patchelf/patcher.rb#179
  def save(out_file = T.unsafe(nil), patchelf_compatible: T.unsafe(nil)); end

  # Get the soname of a shared library.
  #
  # @example
  #   patcher = PatchELF::Patcher.new('/bin/ls')
  #   patcher.soname
  #   # [WARN] Entry DT_SONAME not found, not a shared library?
  #   #=> nil
  # @example
  #   PatchELF::Patcher.new('/lib/x86_64-linux-gnu/libc.so.6').soname
  #   #=> "libc.so.6"
  # @return [String?] The name.
  #
  # source://patchelf//lib/patchelf/patcher.rb#118
  def soname; end

  # Set soname.
  #
  # If the input ELF is not a shared library with a soname,
  # this method will show a warning and has no effect.
  #
  # @note This setting will be saved after {#save} being invoked.
  # @param name [String]
  #
  # source://patchelf//lib/patchelf/patcher.rb#128
  def soname=(name); end

  # Set all operations related to DT_RUNPATH to use DT_RPATH.
  #
  # @return [self]
  #
  # source://patchelf//lib/patchelf/patcher.rb#168
  def use_rpath!; end

  private

  # @return [Boolean]
  #
  # source://patchelf//lib/patchelf/patcher.rb#228
  def dirty?; end

  # source://patchelf//lib/patchelf/patcher.rb#242
  def dynamic_or_log; end

  # source://patchelf//lib/patchelf/patcher.rb#202
  def interpreter_; end

  # @raise [exception]
  #
  # source://patchelf//lib/patchelf/patcher.rb#196
  def log_or_raise(msg, exception = T.unsafe(nil)); end

  # @return [Array<String>]
  #
  # source://patchelf//lib/patchelf/patcher.rb#210
  def needed_; end

  # @return [String?]
  #
  # source://patchelf//lib/patchelf/patcher.rb#218
  def runpath_(rpath_sym = T.unsafe(nil)); end

  # @return [String?]
  #
  # source://patchelf//lib/patchelf/patcher.rb#223
  def soname_; end

  # source://patchelf//lib/patchelf/patcher.rb#232
  def tag_name_or_log(type, log_msg); end
end

# Internal use only.
#
# For {Patcher} to do patching things and save to file.
#
# @private
#
# source://patchelf//lib/patchelf/saver.rb#16
class PatchELF::Saver
  # Instantiate a {Saver} object.
  #
  # @param in_file [String]
  # @param out_file [String]
  # @param set [{Symbol => String, Array}]
  # @return [Saver] a new instance of Saver
  #
  # source://patchelf//lib/patchelf/saver.rb#24
  def initialize(in_file, out_file, set); end

  # @return [String] Input filename.
  #
  # source://patchelf//lib/patchelf/saver.rb#17
  def in_file; end

  # @return [String] Output filename.
  #
  # source://patchelf//lib/patchelf/saver.rb#18
  def out_file; end

  # @return [void]
  #
  # source://patchelf//lib/patchelf/saver.rb#37
  def save!; end

  private

  # source://patchelf//lib/patchelf/saver.rb#278
  def dynamic; end

  # source://patchelf//lib/patchelf/saver.rb#158
  def expand_dynamic!; end

  # This can only be used for patching interpreter's name
  # or set strings in a malloc-ed area.
  # i.e. NEVER intend to change the string defined in strtab
  #
  # source://patchelf//lib/patchelf/saver.rb#238
  def inline_patch(off, str); end

  # Create a temp tag header.
  #
  # @return [ELFTools::Structs::ELF_Dyn]
  #
  # source://patchelf//lib/patchelf/saver.rb#150
  def lazy_dyn(sym); end

  # source://patchelf//lib/patchelf/saver.rb#179
  def malloc_strtab!; end

  # source://patchelf//lib/patchelf/saver.rb#88
  def patch_dynamic; end

  # source://patchelf//lib/patchelf/saver.rb#53
  def patch_interpreter; end

  # source://patchelf//lib/patchelf/saver.rb#121
  def patch_needed; end

  # Modify the out_file according to registered patches.
  #
  # source://patchelf//lib/patchelf/saver.rb#243
  def patch_out(out_file); end

  # source://patchelf//lib/patchelf/saver.rb#111
  def patch_runpath(sym = T.unsafe(nil)); end

  # source://patchelf//lib/patchelf/saver.rb#103
  def patch_soname; end

  # @param str [String]
  # @yieldparam idx [Integer]
  # @yieldreturn [void]
  #
  # source://patchelf//lib/patchelf/saver.rb#208
  def reg_str_table(str, &block); end

  # @return [ELFTools::Sections::Section?]
  #
  # source://patchelf//lib/patchelf/saver.rb#271
  def section_header(name); end

  # source://patchelf//lib/patchelf/saver.rb#217
  def strtab_string; end
end

# To mark a not-using tag
#
# source://patchelf//lib/patchelf/saver.rb#120
PatchELF::Saver::IGNORE = T.let(T.unsafe(nil), Integer)

# Current gem version.
#
# source://patchelf//lib/patchelf/version.rb#5
PatchELF::VERSION = T.let(T.unsafe(nil), String)
